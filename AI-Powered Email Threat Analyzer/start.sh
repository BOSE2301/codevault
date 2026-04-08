#!/bin/bash

# --- start.sh ---
# This script builds and runs the AI Phishing Analyzer Docker container.

# Set the name for our Docker image
IMAGE_NAME="phishing-analyzer:latest"

#
# --- Step 1: Check if Docker is running ---
#
echo "Checking if Docker daemon is running..."
if ! docker info > /dev/null 2>&1; then
    echo " Docker is not running."
    echo "Please start Docker Desktop and try again."
    exit 1
fi
echo "Docker is running."

#
# --- Step 2: Check for the .env file ---
#
if [ ! -f .env ]; then
    echo " .env file not found."
    echo "Please create a .env file with your secrets before running."
    exit 1
fi
echo " .env file found."

#
# --- Step 3: Build the Docker image ---
#
echo " Building Docker image: $IMAGE_NAME"
docker build -t $IMAGE_NAME .
# Check if the build was successful
if [ $? -ne 0 ]; then
    echo " Docker build failed. Please check the Dockerfile and logs."
    exit 1
fi
echo " Docker image built successfully."

#
# --- Step 4: Run the Docker container ---
#
echo "Launching the application..."
echo "Your application will be available at: http://127.0.0.1:7860"
echo "Press CTRL+C in this window to stop the application."
docker run --rm -p 7860:7860 --name phishing-analyzer-container --env-file .env $IMAGE_NAME

echo "Application stopped."