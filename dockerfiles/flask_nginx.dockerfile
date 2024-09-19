FROM tiangolo/uwsgi-nginx-flask:python3.12

ENV UWSGI_INI /config/uwsgi.ini

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./app /app/app
COPY ./static /app/static
COPY ./config /config