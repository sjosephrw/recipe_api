FROM python:3.9.5-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# If we do not add the line below and the container is compromised the attacker will get roor access
RUN adduser -D user
USER user
