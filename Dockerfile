# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Default command to run tests
#CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]
CMD ["pytest", "tests/"]
