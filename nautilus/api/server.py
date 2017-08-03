# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os

import falcon
from oslo_config import cfg
from oslo_log import log
from paste import deploy
from paste import urlmap

from nautilus.api import request
from nautilus.common.i18n import _


CONF = cfg.CONF
LOG = log.getLogger(__name__)


def launch():
    application = falcon.API(request_type=request.Request)
    return application


def get_wsgi_app(config_path=None, **kwargs):
    config_file = kwargs.get('config_file', 'nautilus.conf')
    paste_file = kwargs.get('paste_file', 'nautilus-paste.ini')

    if config_path is None:
        config_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), '../../etc')

    config_file = os.path.join(config_path, config_file)
    global_config = {'config_file': config_file}

    LOG.debug(_('Starting WSGI application using configuration from %s',
                config_path))

    return deploy.loadapp('config:%s' % paste_file,
                          relative_to=config_path,
                          global_config=global_config)


if __name__ == '__main__':
    from wsgiref import simple_server
    wsgi_app = get_wsgi_app()
    httpd = simple_server.make_server('127.0.0.1', 9900, wsgi_app)
    httpd.serve_forever()
