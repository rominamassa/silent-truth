FROM python:3.11-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Use the shell form so that $PORT is substituted
CMD gunicorn app:app --bind 0.0.0.0:$PORT