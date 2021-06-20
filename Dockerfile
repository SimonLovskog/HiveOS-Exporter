FROM python:alpine
WORKDIR /app

RUN apk --update --no-cache add g++ && rm -f /var/cache/apk/*

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app
ENTRYPOINT [ "python", "main.py" ]