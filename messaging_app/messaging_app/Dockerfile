# Use the base Python image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Install gcc
RUN apt-get update && apt-get install -y gcc

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code into the container
COPY . /app/

# Expose the port that the app runs on
EXPOSE 8000

# Run the Django app and map ports
ENTRYPOINT ["sh", "-c", "python manage.py runserver 0.0.0.0:8000 -p 8000:8000"]
