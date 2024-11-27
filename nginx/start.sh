#!/bin/bash
cat /tmp/default.conf | envsubst '$FLASK_SERVER_ADDR' | envsubst '$FILE_SERVER_ADDR' > /etc/nginx/conf.d/default.conf && \
nginx -g 'daemon off;'
