FROM python:3.8-alpine

WORKDIR /app

RUN apk update && apk add --no-cach --virtual bash git gcc g++

RUN python -m pip install --upgrade pip

COPY requirements.txt /app

RUN python -m pip install -r requirements.txt

COPY . /app

CMD ["python3", "manage.py", "runserver"]