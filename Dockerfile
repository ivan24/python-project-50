FROM python:latest

RUN python3 -m pip install poetry==1.1.13
RUN python3 -m pip install install flake8==5.0.4
WORKDIR /code