# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    zlib1g-dev \
    && pip install --no-cache-dir fastapi[all] torch transformers Pillow uvicorn

# Copy the current directory contents into the container at /app
COPY . /app

# Set environment variable for the application
ENV MODEL_PATH /app/clip-vit-base-patch16

# Expose the port that the app will run on
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

