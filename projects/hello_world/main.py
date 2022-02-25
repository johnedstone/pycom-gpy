"""
Device:
    Gpy (firmware, latest: shipped with CAT-M1 5.4.1.0-50523) on
    Pytrack 2 (firmware, latest: pytrack2_v16.dfu)
"""
import time

from helper_functions import get_hello_world

print('Starting "Hello World Project"')
'''
while True:
    print('Starting "Hello World Project"')
    try:
        msg = hello_world()
        print(f'{msg}')
    except Exception as e:
        print(f'{e}')
    finally:
        time.sleep(1)
'''
# vim: ai et ts=4 sts=4 sw=4 nu
