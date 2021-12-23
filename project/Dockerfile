# pull official base image
FROM python:3.9.6-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean \
  && mkdir -p /usr/src/app

# install python dependencies
ADD ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# add app
ADD . .