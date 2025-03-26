# Use an official Python runtime as a parent image
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

EXPOSE 80

# Increase the timeout to 18000 seconds (5hrs)
CMD ["gunicorn", "-b", "0.0.0.0:80", "--timeout", "18000", "app:app"]
