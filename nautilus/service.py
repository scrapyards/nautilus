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

import functools
import sys

from oslo_log import log
from paste import deploy

from nautilus.api import wsgi

LOG = log.getLogger(__name__)


def fail_gracefully(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            LOG.critical(e)
            sys.exit(1)


@fail_gracefully
def v1_app_factory(global_config, **local_config):
    return wsgi.launch_app_v1()

@fail_gracefully
def version_factory(global_config, **local_config):
    return wsgi.launch_app_v1()
