FROM python:3.7.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /drf-with-auth

COPY Pipfile Pipfile.lock /drf-with-auth/
RUN pip install pipenv && pipenv install --system

COPY . /drf-with-auth/