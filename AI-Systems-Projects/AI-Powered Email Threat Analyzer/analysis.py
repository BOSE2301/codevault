import json
from groq import Groq
from langsmith import traceable
@traceable(name="Phishing AI Verdict")
def get_ai_verdict(parsed_data, groq_client):
    if not groq_client: return {"error": "Groq client not provided."}
    prompt_data = {"authentication": {"SPF": parsed_data['headers'].get('spf'),"DKIM": parsed_data['headers'].get('dkim')},"metadata": {"Subject": parsed_data['headers']['Subject'],"From": parsed_data['headers']['From']},"content_summary": {"url_count": len(parsed_data['urls']),"first_few_urls": parsed_data['urls'][:5],"body_snippet": parsed_data['body_text'][:1500]}}
    prompt = f'You are a JSON-generating security analyst. Analyze the following data and return ONLY a single, valid JSON object based on the requested schema. Do not add any extra text or explanations.\n\n**Data to Analyze:**\n```json\n{json.dumps(prompt_data, indent=2)}\n```\n\n**Required JSON Output Schema:**\n```json\n{{"verdict": "string (one of: \'Benign\', \'Suspicious\', \'Malicious\', \'Promotional Newsletter\')","confidence_score": "integer (0-100)","summary": "string (A one-paragraph summary of your findings.)","red_flags": [{{"flag": "string (e.g., \'Authentication Failure\')","details": "string (Explain why this is a red flag.)"}}]}}\n```'
    try:
        chat_completion = groq_client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama3-70b-8192", temperature=0.1, response_format={"type": "json_object"})
        return json.loads(chat_completion.choices[0].message.content)
    except Exception as e: return {"error": f"AI analysis failed: {e}"}