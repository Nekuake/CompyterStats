import psutil
import time
import os


def get_cpu_freq():
    # current, min, max
    cpu = psutil.cpu_freq()
    return cpu


def get_cpu_load(interval):
    load_list = psutil.cpu_percent(interval=interval,percpu=True)
    return load_list

example=get_cpu_load()
print (example)