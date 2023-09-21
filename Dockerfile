FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip build-essential python3 ffmpeg libsm6 libxext6

COPY requirements.txt requirements.txt
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["python3"]
CMD ["wsgi.py"]
