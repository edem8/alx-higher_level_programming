#!/usr/bin/python3

def safe_print_divission(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    if result:
        return result
    else:
        return None
