from builtins import print as _print

# Prints text to stdout.
def print(*args, **kwargs):

    if "flush" in kwargs:
        del kwargs["flush"]

    _print(*args, **kwargs, flush=True)