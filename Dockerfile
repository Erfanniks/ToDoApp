# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /usr/src/app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /usr/src/app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for database URL
ENV DATABASE_URL=postgresql://postgres:postgres@postgres/todolistdb

# Run gunicorn when the container launches
CMD ["gunicorn", "src.run:app", "--bind", "0.0.0.0:5000"]
