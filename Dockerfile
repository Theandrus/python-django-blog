FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /final_task

WORKDIR /final_task

COPY requirements.txt /final_task/

RUN pip install --upgrade pip && pip install -r requirements.txt