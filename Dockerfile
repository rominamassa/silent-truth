FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your application code
COPY . .

# Specify the command to run your app using Gunicorn.
# This assumes your Flask app instance is named "app" in app.py.
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:$PORT"]
