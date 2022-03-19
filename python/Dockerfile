ARG NAME_FILE=entrypoint
ARG NAME_APP=app

FROM python:3 as local

ENV PYTHONPATH=/usr/src/app
ENV PYTHONUNBUFFERED True
ENV APP_HOME /usr/src/app
ENV PORT=8080

WORKDIR /usr/src/app

COPY . .
RUN pip install -r requirements.txt


FROM python:3.10-slim as builder
ENV PYTHONPATH=/usr/src/app
ENV PYTHONUNBUFFERED True
ENV APP_HOME /usr/src/app
WORKDIR $APP_HOME
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt


FROM builder as production
RUN pip install --no-cache-dir -r requirements.txt
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 $NAME_FILE:NAME_APP