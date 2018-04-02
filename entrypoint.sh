#!/bin/bash
set +ex

PORT=${PORT:-9000}
API_WORKERS=${API_WORKERS:="4"}
API_THREADS=${API_THREADS:="1"}

exec uwsgi --http 0.0.0.0:$PORT \
           --wsgi-file /var/lib/openstack/bin/nautilus-wsgi \
           --enable-threads -L \
           --threads ${API_THREADS} \
           --workers ${API_WORKERS}
