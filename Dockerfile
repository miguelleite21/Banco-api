
FROM python:3.8-slim-buster
WORKDIR /code
ENV FLASK_APP=code:/app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
RUN ls -la app/
CMD [ "python", "-m", "flask","run","--host=0.0.0.0"]
