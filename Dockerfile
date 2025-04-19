FROM python:3.12-alpine

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

CMD python app.py