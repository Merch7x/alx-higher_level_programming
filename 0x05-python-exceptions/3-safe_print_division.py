#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        a / b
    except (ZeroDivisionError):
        return None
    else:
        result = a / b
        return result
    finally:
        print("Inside result:{}".format(result))
