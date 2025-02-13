# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose port 5000 for the app
EXPOSE 5000

# Step 6: Run the Flask app
CMD ["python", "app.py"]
