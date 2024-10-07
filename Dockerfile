FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gettext build-essential git wget && apt-get update

RUN mkdir -p /app/requirements

WORKDIR /app

COPY requirements.txt /app/.

RUN pip install --no-cache-dir -U pip setuptools \
 && pip install --no-cache-dir -r requirements.txt

COPY . /app/.


CMD ["gunicorn", "app_settings.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
