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

import falcon
from oslo_config import cfg
from oslo_log import log

from nautilus.api import request
from nautilus.api import v1
from nautilus.api.common import middleware
from nautilus.common import policy


CONF = cfg.CONF
LOG = log.getLogger(__name__)


def configure_app(app, version=''):

    policy.setup_policy()

    for path, res in v1.endpoints():
        app.add_route('%s%s' % (version, path), res)

    return app


def nautilus_app_factory(global_config, **local_config):

    middleware_list = list()
    middleware_list.append(middleware.JSONTranslator())

    app = falcon.API(request_type=request.Request,
                     middleware=middleware_list)

    return configure_app(app, version='/v1')
