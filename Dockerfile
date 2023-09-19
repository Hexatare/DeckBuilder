# syntax=docker/dockerfile:1

FROM python:slim-bullseye

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "wsgi.py"]

