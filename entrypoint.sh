#! /usr/bin/env sh
set -e

/uwsgi-nginx-entrypoint.sh

mv /nginx/nginx.conf /etc/nginx/conf.d/nginx.conf

exec "$@"