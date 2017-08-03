import os

from keystonemiddleware import opts
from oslo_config import cfg
from oslo_log import log
from oslo_policy import policy

from nautilus import version

CONF = cfg.CONF

def parse_args(args=[]):

    paste_grp = cfg.OptGroup('paste_deploy', 'Paste Configuration')

    policy.Enforcer(CONF)
    default_config_files = cfg.find_config_files('nautilus', 'nautilus-api')


def setup_logging():
    _DEFAULT_LOG_LEVELS = ['requests.packages.urllib3.connectionpool=WARN',
                           'urllib3.connectionpool=WARN',
                           'keystonemiddleware=WARN']
    _DEFAULT_LOGGING_CONTEXT_FORMAT = ('%(asctime)s.%(msecs)03d %(process)d '
                                       '%(levelname)s %(name)s [%(request_id)s'
                                       ' %(user_identity)s] %(instance)s '
                                       '%(message)s')
    log.set_defaults(_DEFAULT_LOGGING_CONTEXT_FORMAT, _DEFAULT_LOG_LEVELS)
    log.setup(CONF, 'nautilus', version=version.version_info)

def find_paste_config():
    if CONF.paste_deploy.config_file:

    return paste_config

def list_opts():
    _OPTS = {
        'paste_deploy': paste_deploy,
        AUTH_GROUP: AUTH_OPTS
    }

    return _OPTS.items()
