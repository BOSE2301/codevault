#  PhishSleuth

> AI-Powered Email Threat Analyzer (Dockerized)

PhishSleuth is an end-to-end email analysis tool that uses AI (via Groq LLMs) to detect phishing, spam, and other suspicious email behaviors. Just upload a `.eml` file and receive an intelligent verdict, confidence score, and red flags. This project is Docker-ready and integrates with AWS S3 and LangSmith for cloud storage and observability.

---

##  Features

-  Upload and analyze `.eml` email files
-  AI-generated verdicts using Groq (via LLaMA3-70B)
-  Checks SPF, DKIM, and DMARC authentication headers
- ☁ Uploads reports and email files to AWS S3
-  LangSmith tracing enabled for observability
-  Fully Dockerized application for easy deployment

---

## Setup Instructions
- Create and activate a virtual environment
- python3 -m venv venv
- source venv/bin/activate
- Install dependencies
- pip install -r requirements.txt
- Create a .env file

---

## RUN Locally 
- python app.py
## Docker Setup
Build and Run via script
- bash start.sh
- bash stop.sh
