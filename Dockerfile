FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python3 python3-pip -y
RUN pip3 install --upgrade pip

# Set the working directory in the container
WORKDIR /app

ENV DB_USERNAME=postgres \
    DB_PASSWORD=mypassword \
    DB_HOST=localhost \
    DB_PORT=5432 \
    DB_NAME=postgres

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .


# Expose the port the Flask app will run on
EXPOSE 80


# Run the Fast API app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]