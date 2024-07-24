FROM python:3.7.8-slim

# Expose the port your app will run on
EXPOSE 8080

# Upgrade pip
RUN pip install -U pip

# Copy requirements file into the app directory
COPY requirements.txt app/requirements.txt

# Install the required packages
RUN pip install -r app/requirements.txt

# Copy the rest of the application files into the app directory
COPY . /app

# Set the working directory
WORKDIR /app

# Run the application
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
