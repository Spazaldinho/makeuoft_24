# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Install system dependencies required for OpenCV and GLib
# Also, perform cleanup in the same RUN statement to minimize image size
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Configure Streamlit to listen on all interfaces and disable CORS
RUN mkdir -p ~/.streamlit && \
    echo "[server]\n\
    headless = true\n\
    port = $PORT\n\
    enableCORS = false\n\
    " > ~/.streamlit/config.toml

# Expose the port Streamlit will run on
EXPOSE 8080

# Specify a non-root user to run the application (Optional: Create a user or use an existing one)
# RUN adduser --disabled-password --gecos '' myuser
# USER myuser

# The command to run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.enableCORS=false", "--server.headless=true"]

