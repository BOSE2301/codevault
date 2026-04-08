# --- Load environment variables from .env file ---
from dotenv import load_dotenv
load_dotenv()
# ------------------------------------------------------

import gradio as gr, os, json
from concurrent.futures import ThreadPoolExecutor
from groq import Groq
from email_parser import parse_email_content
from analysis import get_ai_verdict
from s3_handler import upload_to_s3

# The rest of the file is identical. os.environ.get() will now find
# the variables that load_dotenv() just loaded.

secrets = {
    "groq": os.environ.get("GROQ_API_KEY"),
    "aws_access_key_id": os.environ.get("AWS_ACCESS_KEY_ID"),
    "aws_secret_access_key": os.environ.get("AWS_SECRET_ACCESS_KEY"),
    "bucket_name": os.environ.get("BUCKET_NAME")
}
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.environ.get("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "Phishing Analyzer (Local Docker)"

groq_client = Groq(api_key=secrets["groq"]) if secrets["groq"] else None

def process_and_analyze(eml_file_object):
    if not all([groq_client, eml_file_object]): return "ERROR: Groq client not authenticated or no file uploaded.", None, None
    try:
        with open(eml_file_object.name, 'rb') as f: eml_content = f.read()
        parsed_data = parse_email_content(eml_content); ai_report = get_ai_verdict(parsed_data, groq_client); sha256_hash = parsed_data['sha256_hash']
        eml_s3_status, report_s3_status, report_string_to_upload = "Upload failed.", "Upload failed.", json.dumps(ai_report, indent=2)
        with ThreadPoolExecutor(max_workers=2) as executor:
            eml_future = executor.submit(upload_to_s3, secrets["aws_access_key_id"], secrets["aws_secret_access_key"], secrets["bucket_name"], eml_content, f"{sha256_hash}.eml")
            report_future = executor.submit(upload_to_s3, secrets["aws_access_key_id"], secrets["aws_secret_access_key"], secrets["bucket_name"], report_string_to_upload.encode('utf-8'), f"{sha256_hash}_report.json")
            eml_s3_status, report_s3_status = eml_future.result(), report_future.result()
        summary_report = f'**File Name:** {os.path.basename(eml_file_object.name)}\n**SHA256 Hash:** `{sha256_hash}`\n### Email Authentication\n- **SPF Check:** {parsed_data["headers"].get("spf", "N/A")}\n- **DKIM Check:** {parsed_data["headers"].get("dkim", "N/A")}\n- **DMARC Check:** {parsed_data["headers"].get("dmarc", "N/A")}'
        cloud_status = f'### Cloud Integration\n- **EML Upload:** {eml_s3_status}\n- **Report Upload:** {report_s3_status}\n- **Observability:** Trace sent to LangSmith project.'
        return summary_report, ai_report, cloud_status
    except Exception as e: return f"An unexpected error occurred: {e}", None, None

with gr.Blocks(theme=gr.themes.Soft()) as iface:
    gr.Markdown("#AI Phishing Analyzer (Dockerized)")
    with gr.Row():
        with gr.Column(scale=1): file_input = gr.File(label="Upload .eml File", file_types=[".eml"]); submit_button = gr.Button("Analyze Email", variant="primary")
        with gr.Column(scale=2): summary_output = gr.Markdown(label="Analysis Summary"); json_output = gr.JSON(label="Groq AI Analysis"); status_output = gr.Markdown(label="Status")
    submit_button.click(fn=lambda: (gr.update(value="Analyzing...", interactive=False), None, None, None), outputs=[submit_button, summary_output, json_output, status_output]).then(fn=process_and_analyze, inputs=file_input, outputs=[summary_output, json_output, status_output]).then(fn=lambda: gr.update(value="Analyze Email", interactive=True), outputs=[submit_button])

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)