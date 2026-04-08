# --- Dockerfile for the Phishing Analyzer ---

# 1. Start with a lightweight and official Python base image.
FROM python:3.11-slim

# 2. Set a working directory inside the container.
# This is where our code will live.
WORKDIR /app

# 3. Copy only the requirements file first to leverage Docker's layer caching.
# If the requirements don't change, Docker won't re-install them every time.
COPY requirements.txt .

# 4. Install the Python dependencies.
# --no-cache-dir keeps the image smaller.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our application source code into the working directory.
COPY . .

# 6. Expose the port that Gradio will run on.
# This is for documentation and can be used for networking.
EXPOSE 7860

# 7. Define the command that will run when the container starts.
CMD ["python", "app.py"]