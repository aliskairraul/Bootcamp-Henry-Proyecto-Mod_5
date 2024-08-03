FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY main.py main.py
COPY pages/ pages/
COPY assets/ assets/
COPY components/ components/
COPY data/ data/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:server", "--log-level", "debug"]

