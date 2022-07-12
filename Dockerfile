
FROM python:3.8-slim-buster
WORKDIR /code
ENV FLASK_APP=app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

