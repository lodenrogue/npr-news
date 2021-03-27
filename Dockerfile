FROM python:3.6-slim

RUN apt-get update

RUN apt-get install -y python-dev

RUN apt-get install -y libxml2-dev libxslt-dev

RUN apt-get install -y libjpeg-dev zlib1g-dev libpng-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV TERM=xterm-256color

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "npr_news.py"] 
