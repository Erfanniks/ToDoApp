# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the necessary files and directories into the container at /usr/src/app
COPY src/ ./src/
COPY requirements.txt .
COPY static/ ./static/
COPY templates/ ./templates/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask application
ENV FLASK_APP=src/run.py DB_USER="" DB_PASSWORD="" DB_HOST="" DB_PORT="" DB_NAME=""


# Run the Flask application with Gunicorn
CMD ["gunicorn", "src.run:app", "--bind", "0.0.0.0:5000"]
