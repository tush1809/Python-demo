# Use official Python base image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run main script
CMD ["python", "src/main.py"]