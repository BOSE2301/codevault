#!/bin/bash

# --- stop.sh ---
# This script finds and stops the running phishing analyzer container.

# Define the name of the container we set in start.sh
CONTAINER_NAME="phishing-analyzer-container"

echo "Searching for container: $CONTAINER_NAME..."

# Check if the container is running
if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
    echo " Container found. Sending stop command..."
    docker stop $CONTAINER_NAME
    echo "Container stopped successfully."
else
    echo "Container '$CONTAINER_NAME' is not running."
fi