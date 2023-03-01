FROM python:3.9-slim

RUN apt-get update && apt-get install -y wget

# Set up a working directory
WORKDIR /app

# Copy requirements.txt and install the dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the bot files to the container
COPY . .

CMD ["python", "firstBot.py"]