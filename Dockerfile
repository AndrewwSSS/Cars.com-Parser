FROM python:3.11.9-alpine3.19
LABEL authors="clash"

RUN apk update && apk add --no-cache \
    chromium \
    chromium-chromedriver

RUN pip install --upgrade pip

ENV CHROME_BIN=/usr/bin/chromium-browser
ENV CHROME_DRIVER=/usr/bin/chromedriver
ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY . .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app/main.py"]