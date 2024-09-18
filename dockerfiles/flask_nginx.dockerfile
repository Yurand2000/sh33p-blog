FROM tiangolo/uwsgi-nginx-flask:python3.12

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./app /app/app
COPY ./static /app/static
COPY ./uwsgi.ini /app/uwsgi.ini
COPY ./.nginx/nginx.conf /nginx/nginx.conf