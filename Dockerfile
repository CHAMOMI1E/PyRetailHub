FROM python:3.11-alpine

LABEL authors="chamomile"

WORKDIR /PyRetailHub

RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    build-base \
    tzdata

RUN ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \
    echo "Europe/Moscow" > /etc/timezone

RUN apk add --no-cache curl

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

RUN poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* ./



RUN poetry install --no-root --no-interaction --no-ansi

COPY ./ ./
COPY ./ .env ./

RUN chmod -R 777 ./