#Dockerfile for minimal image with Python 3.11
FROM python:3.11-slim

# Set the working directory
WORKDIR /app
# Copy the directory zanggasse contents into the container at /app
COPY ./zanggasse /app

#import requests and imaplib
RUN pip install requests 
#RUN pip install imaplib
#when the container is started, the python script main.py will be run
CMD ["python", "main.py"]