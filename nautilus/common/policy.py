import functools

from oslo_policy import policy

from nautilus import exceptions as n_exc

_ENFORCER = None


def setup_policy(conf):
    global _ENFORCER
    if not _ENFORCER:
        _ENFORCER = policy.Enforcer(conf)


def enforce(rule):

    def decorator(func):
        @functools.wraps(func)
        def handler(*args, **kwargs):
            context = args[1].context
            _ENFORCER.enforce(rule, {}, context.to_dict(),
                              do_raise=True,
                              action=rule,
                              exc=n_exc.ActionForbidden)
            return func(*args, **kwargs)
        return handler

    return decorator
