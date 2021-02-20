FROM python:3.7.6

RUN apt-get update

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
ADD manage.py /app/

RUN apt-get --assume-yes install python-dev

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get --assume-yes install pylint
RUN pip install --upgrade autopep8

WORKDIR /app