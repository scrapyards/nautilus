========
Nautilus
========

This project builds out a basic falcon-based WSGI server powered by
OpenStack framework and libraries.  The restFUL calls is backed
by OpenStack Identity service (keystone) with RBAC support.

TODO
----

* Improve configuration files finding
* Enable and improve better logging support
* Add database support
* Unit tests!!!!!!

GETTING STARTED
---------------

To build Nautilus make sure your work is commited to the repo and run the
following from the root of the project:

::

  docker build . \
    --build-arg PROJECT_REF=$(git rev-parse --abbrev-ref HEAD) \
    --tag nautilus:$(git rev-parse --short HEAD)

You can then run the built image using:

::

  docker run --rm \
    --name nautilus \
    --volume $(pwd)/etc:/etc/nautilus:ro \
    --publish 9980:9980/tcp \
    --env PORT=9980 \
    nautilus:$(git rev-parse --short HEAD)
