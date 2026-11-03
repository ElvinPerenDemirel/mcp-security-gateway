# Use an official lightweight Python 3.10 image as a parent image
FROM python:3.10-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Install the required Python packages (pinning mcp to v1 to match our codebase)
RUN pip install --no-cache-dir "mcp<2" fastapi uvicorn requests sentence-transformers

# Copy the project files into the container (ignoring files in .dockerignore)
COPY . /app

# Command to run the agent client when the container starts
CMD ["python", "agent_client.py"]