# Use official Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (better caching)
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY app/ /app/

# Expose the port your Flask app runs on
EXPOSE 8080

# Start the Flask app
CMD ["python", "main.py"]
