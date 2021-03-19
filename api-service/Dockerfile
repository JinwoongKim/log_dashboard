FROM python:3.9.2

WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y vim

RUN pip install uvicorn
RUN pip install fastapi

COPY ./main.py .
RUN chmod +x main.py
RUN mkdir log

EXPOSE 8000
