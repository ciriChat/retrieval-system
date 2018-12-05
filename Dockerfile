FROM python:3.7-slim

WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    gcc

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "gunicorn", "-c", "gunicorn_config.py", "setup:app" ]
