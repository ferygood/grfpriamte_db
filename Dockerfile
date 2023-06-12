# under development, please do not use
# Use the official PostgreSQL image as the base image
FROM python:3.9.17

RUN apt-get update \
    && apt-get install -y postgresql-client

WORKDIR /app

COPY . /app

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD python create_table.py
