import os


MONITOR_DIR = [
    {'sys1': ['d:\p_proj\log_example\dir[12]']},
    {'server2': ['d:\p_proj\log_example\dir4']}
]


class Config(object):
    SECRET_KEY = os.urandom(24)
