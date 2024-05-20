# Use an official Node runtime as a parent image
FROM node:20

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN npm install

# Expose the port that the extension will run on
EXPOSE 3000

# Command to run the extension
CMD ["npm", "run", "start"]
