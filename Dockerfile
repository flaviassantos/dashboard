FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn pymysql

COPY app app
COPY data data
COPY migrations migrations
COPY dashboard.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP dashboard.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]