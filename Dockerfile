# Base image: Selenium standalone with Chrome
FROM selenium/standalone-chrome:latest

# Switch to root to run privileged commands
USER root

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory inside the container
WORKDIR /workspace

# Copy the requirements file to the container
COPY requirements.txt /workspace/

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . /workspace/

# Default command to run the tests
CMD ["pytest", "--alluredir=allure-results"]
