FROM python:3.7.6-buster
LABEL maintainer="redscaresu"

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

RUN groupadd -r redscaresu && useradd -r -s /bin/false -g redscaresu redscaresu

WORKDIR /app

COPY emoji-server.py emoji-cli.py /app/

RUN chown -R redscaresu:redscaresu /app

EXPOSE 12000/udp

USER redscaresu
CMD ["python", "emoji-server.py"]
