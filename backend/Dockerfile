FROM tiangolo/uvicorn-gunicorn:python3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

COPY ./app /app