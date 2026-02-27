# Use official Python image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy everything inside src into container
COPY src/ .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run training script when container starts
CMD ["python", "main.py"]
