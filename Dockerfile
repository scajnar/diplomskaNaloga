FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test files
COPY . .

# Install Google Chrome
RUN apt-get update && \
    apt-get install -y wget gnupg2 unzip && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | awk '{ print $3 }' | cut -d '.' -f 1) && \
    wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION | xargs -I {} wget -q https://chromedriver.storage.googleapis.com/{}/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin && \
    chmod +x /usr/local/bin/chromedriver

# Set environment variables for headless Chrome
ENV DISPLAY=:99

# Run the tests
CMD ["python", "-m", "unittest", "discover"]

