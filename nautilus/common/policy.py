import functools

from oslo_policy import policy

from nautilus import exceptions as exc

ENFORCER = None


def setup_policy(conf):
    global ENFORCER
    ENFORCER = policy.Enforcer(conf)


def enforce(rule):

    def decorator(func):
        @functools.wraps(func)
        def handler(*args, **kwargs):
            context = args[1].env['nautilus.context']
            ENFORCER.enforce(rule, {}, context.to_dict(), do_raise=True,
                             exc=exc.AccessForbidden)
            return func(*args, **kwargs)

        return handler

    return decorator
