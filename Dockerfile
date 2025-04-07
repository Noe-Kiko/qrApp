# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

FROM python:3.9.1-slim as base

COPY application/ /application/
COPY qrApp.py /application/

RUN ls -la /application

COPY requirements.txt /application/

RUN RUN pip install -r /application/requirements.txt

WORKDIR /

# Run the application.
CMD ["python", "-m", "qrApp", "--host=0.0.0.0"]