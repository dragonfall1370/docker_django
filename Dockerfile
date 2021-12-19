FROM python:3.7.12-bullseye 
ENV PYTHONUNBUFFERED=1


WORKDIR /django_loginform

COPY ./requirements.txt /django_loginform/requirements.txt

RUN pip install -r requirements.txt

ADD ./linear /django_loginform/linear