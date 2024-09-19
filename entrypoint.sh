#! /usr/bin/env sh
set -e

/uwsgi-nginx-entrypoint.sh

cp /nginx/nginx.conf /etc/nginx/conf.d/nginx.conf

exec "$@"