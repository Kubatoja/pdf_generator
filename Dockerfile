# Start with an official Python image based on Ubuntu
FROM python:3.9-slim

# Set environment variable to avoid prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary system dependencies for Playwright and other libraries
RUN apt-get update && apt-get install -y \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libfontconfig1 \
    libxext6 \
    libx11-xcb1 \
    libxcb1 \
    libx11-6 \
    libgbm-dev \
    libasound2 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libdrm2 \
    libxshmfence1 \
    libxrender1 \
    ca-certificates \
    fonts-liberation \
    libappindicator3-1 \
    libxshmfence-dev \
    lsb-release \
    wget \
    xdg-utils \
    unzip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python libraries
RUN pip install --upgrade pip && \
    pip install \
    asyncio \
    playwright \
    flask \
    waitress \
    --trusted-host pypi.org --trusted-host files.pythonhosted.org

# Install Playwright browsers
RUN playwright install --with-deps

# Set the working directory for your app
WORKDIR /app

# Copy your application code into the container
COPY . /app

# Expose the port that Flask will run on (default: 5000)
EXPOSE 5000

# Define the entry point to run your Flask app with Waitress
# CMD ["waitress-serve", "--host=0.0.0.0", "--port=5000", "app:app"]
CMD ["python", "run.py"]