# Use a lightweight Python base.
FROM python:3.9-slim

# Set work directory.
WORKDIR /app

# Copy only requirements.txt first.
COPY requirements.txt /app/

# Install Python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . /app

# Expose port 1274.
EXPOSE 1274

# Run Gunicorn.
CMD ["gunicorn", "--bind", "0.0.0.0:1274", "my_project.wsgi:application"]