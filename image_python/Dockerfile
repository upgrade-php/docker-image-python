ARG NAME_FILE=entrypoint
ARG NAME_APP=app

FROM python:3 as local

ENV PYTHONPATH=/usr/src/app
ENV PYTHONUNBUFFERED True
ENV APP_HOME /usr/src/app
ENV PORT=8080

WORKDIR /usr/src/app

COPY . .

RUN pip install -U pip setuptools poetry && \
    poetry config virtualenvs.create

RUN poetry install

FROM python:3.10-slim as builder
ENV PYTHONPATH=/usr/src/app
ENV PYTHONUNBUFFERED True
ENV APP_HOME /usr/src/app
WORKDIR $APP_HOME
COPY . ./
RUN poetry install --no-dev


FROM builder as production
RUN poetry install --no-dev
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 $NAME_FILE:NAME_APP