import email, hashlib, re, html, authres
from email.policy import default
def analyze_authentication_headers(msg):
    auth_header = msg.get("Authentication-Results", "")
    if not auth_header: return {"spf": "Not found", "dkim": "Not found", "dmarc": "Not found"}
    try:
        auth_results = authres.parse(auth_header)
        return {"spf": f"{auth_results.spf.result} (domain: {auth_results.spf.helo or auth_results.spf.smtp_from})", "dkim": f"{auth_results.dkim[0].result} (domain: {auth_results.dkim[0].domain})" if auth_results.dkim else "Not found", "dmarc": f"{auth_results.dmarc.result}" if auth_results.dmarc else "Not found"}
    except Exception: return {"spf": "Parse Error", "dkim": "Parse Error", "dmarc": "Parse Error"}
def parse_email_content(eml_content):
    parsed_data = {}
    parsed_data['sha256_hash'] = hashlib.sha256(eml_content).hexdigest()
    msg = email.message_from_bytes(eml_content, policy=default)
    parsed_data['headers'] = {"Subject": msg.get("Subject", "N/A"), "From": msg.get("From", "N/A"), "To": msg.get("To", "N/A"), "Date": msg.get("Date", "N/A"), "Return-Path": msg.get("Return-Path", "N/A")}
    auth_status = analyze_authentication_headers(msg)
    parsed_data['headers'].update(auth_status)
    plain_text_body, html_body, attachments = None, None, []
    for part in msg.walk():
        if "attachment" not in str(part.get("Content-Disposition")):
            if part.get_content_type() == "text/plain": plain_text_body = part.get_payload(decode=True).decode(errors='ignore')
            elif part.get_content_type() == "text/html": html_body = part.get_payload(decode=True).decode(errors='ignore')
        else:
            if filename := part.get_filename(): attachments.append({"filename": filename, "sha256": hashlib.sha256(part.get_payload(decode=True)).hexdigest()})
    final_body = plain_text_body or (re.sub('<[^<]+?>', ' ', html_body) if html_body else "")
    source_for_urls = html_body or final_body
    url_pattern = r'https?://[^\s<>"\']+'
    decoded_urls = [html.unescape(url) for url in re.findall(url_pattern, source_for_urls)]
    parsed_data['urls'] = list(set(decoded_urls)); parsed_data['attachments'] = attachments; parsed_data['body_text'] = final_body
    return parsed_data
