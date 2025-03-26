# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory in the container
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose the port that the app runs on
EXPOSE 80

# Command to run the Flask app using Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80", "--workers", "3"]
