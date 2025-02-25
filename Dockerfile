FROM python:3.11-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your code
COPY . .

# Run your app with Gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]