# Use the latest official Ubuntu image as the base
FROM ubuntu:latest

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python 3 and CA certificates (no third-party packages needed)
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user for better security
RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser

# Copy the script into the image
COPY --chown=appuser:appuser script.py .

# Run the script when the container starts
CMD ["python3", "script.py"]