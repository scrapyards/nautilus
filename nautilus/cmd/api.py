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
import sys

import falcon
from oslo_config import cfg
from oslo_log import log
from paste import deploy
from paste import httpserver

from nautilus.common.i18n import _
from nautilus.common import config
from nautilus.common import policy
from nautilus import exceptions as n_exc


CONF = cfg.CONF
LOG = log.getLogger(__name__)


def config_app(app):


def main():
    confg.parse_args(args=sys.argv[1:])
    config.setup_logging()
    paste_conf = config.find_paste_config()

    ip = CONF.get('bind_host', '0,0,0,0')
    port = CONF.get('bind_port', 9999)

    try:


    except KeyboardInterrupt:
        print(_("Bye!"))
        sys.exit(0)


if __name__ == '__main__':
    main()
