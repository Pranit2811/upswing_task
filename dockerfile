FROM python:3.8-slim

# RUN apk add --update gcc g++ git libffi-dev postgresql-dev supervisor

RUN apt-get update && apt-get install -y supervisor

COPY ./src/requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./src/ /home/src/
WORKDIR /home/src

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN mkdir -p /var/log/supervisor

ENV ENV=development
ENV PYTHONUNBUFFERED=True
ENV PYTHONDONTWRITEBYTECODE=1

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
