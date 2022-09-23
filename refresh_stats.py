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

def get_process_list():
    process_list=[]
    for proc in psutil.process_iter():
        try:
            current_psutil_process=psutil.Process(proc.pid)
            with current_psutil_process.oneshot():
                pass
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

example=get_cpu_load()
print (example)