# Get the python image from Docker Hub
FROM python:3.8

# Specify the working directory
WORKDIR /code

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy source code and unit tests
COPY src/ ./src/
COPY tests/ ./tests/
