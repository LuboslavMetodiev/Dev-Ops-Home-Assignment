# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

#copy the requirenments
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]