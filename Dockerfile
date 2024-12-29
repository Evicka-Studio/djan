# Use a lightweight Python base.
FROM python:3.9-slim

# Set work directory.
WORKDIR /app

# Copy project files (adjust paths as needed).
COPY . /app

# Install Python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 (Django default or your choice).
EXPOSE 8000

# Run Gunicorn serving the wsgi application.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "my_project.wsgi:application"]