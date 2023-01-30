#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a/b
    except ZeroDivivisionError:
        result = None;
    finally:
        print("Inside resulti:{}".format(result))
    return result

