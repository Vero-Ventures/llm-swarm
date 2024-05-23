# Use an official Node runtime as a parent image
FROM node:20

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN npm install

# Install Python and other necessary tools
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    nox \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv /app/venv

# Activate the virtual environment and install Python dependencies
RUN /bin/bash -c "source /app/venv/bin/activate && pip install -r /app/src/test/python_tests/requirements.txt && pip install nox"

# Run nox setup session
RUN /bin/bash -c "source /app/venv/bin/activate && nox --session setup"

# Expose the port that the extension will run on
EXPOSE 3000

# Command to run the extension
CMD ["npm", "run", "start"]
