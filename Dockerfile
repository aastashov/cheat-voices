FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt

RUN set -x \
    && pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app
