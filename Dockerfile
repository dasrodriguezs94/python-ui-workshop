# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing pyc files and buffer output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the user to root (default)
USER root

# Copy the requirements.txt file into the container
COPY requirements.txt ./

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    xvfb \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libxkbcommon0 \
    libgbm1 \
    libpango-1.0-0 \
    libasound2 \
    fonts-liberation \
    libappindicator3-1 \
    lsb-release \
    xdg-utils \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python and Playwright dependencies
RUN pip install --upgrade pip
RUN pip install pytest pytest-playwright allure-pytest
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright and its browser dependencies
RUN playwright install --with-deps

# Set up the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose ports for Allure reports if needed
EXPOSE 8000

# By default, the command will be empty and you can provide the command to run tests when you execute the container
CMD ["pytest", "--alluredir=allure-results", "playwright_module/tests/"]
