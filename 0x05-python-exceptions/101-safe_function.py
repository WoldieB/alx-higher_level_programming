#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as w:
        sys.stderr.write("Exception: {}\n".format(w))
        result = None

    return (result)
