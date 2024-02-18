# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Install system dependencies required for OpenCV and other functionalities
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the local code to the container image.
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable for Streamlit to use during runtime
ENV PORT=8080

# Configure Streamlit to listen on all interfaces and disable CORS
RUN mkdir -p ~/.streamlit && \
    echo "[server]\n\
    headless = true\n\
    port = $PORT\n\
    enableCORS = false\n\
    " > ~/.streamlit/config.toml

# Command to run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.enableCORS=false", "--server.headless=true"]

