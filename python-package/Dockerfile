# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files into the working directory
COPY pyproject.toml poetry.lock /app/

# Copy the rest of the application code into the container
COPY python-package /app/python-package

# Install build-essential for compiling packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Change to the directory containing the pyproject.toml file
WORKDIR /app

# Install any needed packages specified in pyproject.toml
RUN poetry install --no-root

# Set the PYTHONPATH environment variable
ENV PYTHONPATH="/app/python-package/src"

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "cli"]
