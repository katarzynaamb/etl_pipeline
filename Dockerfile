FROM python:3.9.6-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "bash", "-c", "./entrypoint.sh" ]