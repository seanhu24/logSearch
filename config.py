import os


MONITOR_DIR = [
    {'sys1': ['d:\p_proj\log_example\dir1', 'd:\p_proj\log_example\dir4']},
    {'server2': ['d:\p_proj\log_example\dir2']}
]


class Config(object):
    SECRET_KEY = os.urandom(24)
