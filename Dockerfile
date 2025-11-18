FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src ./src
COPY entrypoint.sh ./entrypoint.sh

# Permissions
RUN chmod +x ./entrypoint.sh

# Volume for data output
VOLUME /app/data

# Entry script
ENTRYPOINT ["./entrypoint.sh"]
