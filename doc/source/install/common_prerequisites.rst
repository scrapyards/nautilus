Prerequisites
-------------

Before you install and configure the thunder service,
you must create a database, service credentials, and API endpoints.

#. To create the database, complete these steps:

   * Use the database access client to connect to the database
     server as the ``root`` user:

     .. code-block:: console

        $ mysql -u root -p

   * Create the ``nautilus`` database:

     .. code-block:: none

        CREATE DATABASE nautilus;

   * Grant proper access to the ``nautilus`` database:

     .. code-block:: none

        GRANT ALL PRIVILEGES ON nautilus.* TO 'nautilus'@'localhost' \
          IDENTIFIED BY 'NAUTILUS_DBPASS';
        GRANT ALL PRIVILEGES ON nautilus.* TO 'nautilus'@'%' \
          IDENTIFIED BY 'NAUTILUS_DBPASS';

     Replace ``NAUTILUS_DBPASS`` with a suitable password.

   * Exit the database access client.

     .. code-block:: none

        exit;

#. Source the ``admin`` credentials to gain access to
   admin-only CLI commands:

   .. code-block:: console

      $ . admin-openrc

#. To create the service credentials, complete these steps:

   * Create the ``nautilus`` user:

     .. code-block:: console

        $ openstack user create --domain default --password-prompt nautilus

   * Add the ``admin`` role to the ``nautilus`` user:

     .. code-block:: console

        $ openstack role add --project service --user nautilus admin

   * Create the nautilus service entities:

     .. code-block:: console

        $ openstack service create --name nautilus --description "thunder" thunder

#. Create the thunder service API endpoints:

   .. code-block:: console

      $ openstack endpoint create --region RegionOne \
        thunder public http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        thunder internal http://controller:XXXX/vY/%\(tenant_id\)s
      $ openstack endpoint create --region RegionOne \
        thunder admin http://controller:XXXX/vY/%\(tenant_id\)s
