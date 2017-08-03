2. Edit the ``/etc/nautilus/nautilus.conf`` file and complete the following
   actions:

   * In the ``[database]`` section, configure database access:

     .. code-block:: ini

        [database]
        ...
        connection = mysql+pymysql://nautilus:NAUTILUS_DBPASS@controller/nautilus
