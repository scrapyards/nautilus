#!/bin/bash
set +ex
exec uwsgi --http 0.0.0.0:$PORT \
           --wsgi-file /var/lib/openstack/bin/nautilus-wsgi
