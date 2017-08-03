import functools

from oslo_config import cfg
from oslo_policy import policy

from nautilus import exceptions as n_exc
from nautilus.common import policies


CONF = cfg.CONF
_ENFORCER = None


def setup_policy():
    global _ENFORCER
    if not _ENFORCER:
        _ENFORCER = policy.Enforcer(CONF)
        register_rules(_ENFORCER)


def enforce(rule):

    setup_policy()

    def decorator(func):
        @functools.wraps(func)
        def handler(*args, **kwargs):
            context = args[1].context
            _ENFORCER.enforce(rule, {}, context.to_dict(),
                              do_raise=True,
                              exc=n_exc.ActionForbidden)
            return func(*args, **kwargs)
        return handler

    return decorator


def register_rules(enforcer):
    enforcer.register_defaults(policies.list_rules())
