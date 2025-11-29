FROM python:3.10
WORKDIR /app

COPY app.py /app

RUN pip install flask psycopg2 redis

CMD ["python", "app.py"]