FROM python:3.7.6-buster

ENV PYTHONUNBUFFERED=1

COPY emoji-server.py emoji-cli.py /

EXPOSE 12000/udp

CMD ["python", "emoji-server.py"]
