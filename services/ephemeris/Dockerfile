FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV LISTEN_ADDR=[::]:80

CMD [ "python3", "server.py"]