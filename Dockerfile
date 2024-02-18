# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Install system dependencies required for opencv
RUN apt-get update && apt-get install -y libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable for Streamlit to use during runtime
ENV PORT=8080

# Use setup.sh to configure streamlit settings
RUN chmod +x ./setup.sh
RUN ./setup.sh

# Run app.py when the container launches
CMD streamlit run app.py --server.port $PORT --server.enableCORS=false --server.headless=true

