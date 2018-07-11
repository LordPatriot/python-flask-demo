FROM ubuntu

LABEL maintainer="orekhov.volodya@gmail.com"

RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential

RUN pip install --upgrade pip 
RUN pip install flask

EXPOSE 5000

COPY . / 
ENTRYPOINT python app.py
