# Use an official Python runtime as a parent image
FROM python:3.7.17

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /Product

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

RUN pip install django
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

RUN pip install gunicorn
# Start Gunicorn with your Django project
#CMD ["gunicorn", "--bind", "0.0.0.0:8080", "Product.wsgi:application"]
#CMD ["gunicorn"]
#CMD ["gunicorn", "--bind", "8080:8080", "Product.wsgi"]
# Expose the Gunicorn port (you can modify this if needed)
#EXPOSE 8000

# Define the command to run Gunicorn with your project
#CMD ["gunicorn", "-c", "conf/gunicorn_config.py", "Product.wsgi"]
#CMD ["gunicorn", "--bind", "0.0.0.0:8080", "Product.wsgi:application"]
