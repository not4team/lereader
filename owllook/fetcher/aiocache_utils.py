import inspect
from aiocache import Cache, caches


def _get_cache(cache=Cache.REDIS, serializer=None, plugins=None, **cache_kwargs):
    cache = cache or caches.get('default')
    return cache

def _get_args_dict(func, args, kwargs):
    defaults = {
        arg_name: arg.default
        for arg_name, arg in inspect.signature(func).parameters.items()
        if arg.default is not inspect._empty  # TODO: bug prone..
    }
    args_names = func.__code__.co_varnames[: func.__code__.co_argcount]
    return {**defaults, **dict(zip(args_names, args)), **kwargs}
