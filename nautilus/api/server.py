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

import logging as py_logging
import os

import falcon
from oslo_config import cfg
from oslo_log import log
from paste import deploy
from paste import urlmap
from wsgiref import simple_server

from nautilus.api import request
from nautilus.common.i18n import _


CONF = cfg.CONF
LOG = log.getLogger(__name__)


def setup_logging(conf):

    # Add additional dependent libraries that have unhelp bug levels
    extra_log_level_defaults = []

    log.set_defaults(default_log_levels=log.get_default_log_levels() +
                     extra_log_level_defaults)
    log.setup(conf, 'nautilus')
    py_logging.captureWarnings(True)


def init_application(base=None, **kwargs):
    config_file = kwargs.get('config_file', 'nautilus.conf')
    config_path = kwargs.get('config_path', None)
    paste_file = kwargs.get('paste_file', 'nautilus-paste.ini')

    # TODO(lamt) Enable the logging load
    # setup_logging(CONF)

    if config_path is None:
        config_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), '../../etc')

    config_file = os.path.join(config_path, config_file)
    global_config = {'config_file': config_file}

    LOG.debug(_('Starting WSGI application using configuration from %s'),
              config_path)

    return deploy.loadapp('config:%s' % paste_file,
                          relative_to=config_path)


def launch():
    wsgi_app = init_application()
    httpd = simple_server.make_server('127.0.0.1', 9900, wsgi_app)
    httpd.serve_forever()


if __name__ == '__main__':
    launch()
