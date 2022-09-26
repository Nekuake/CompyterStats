import json

import psutil
import time
import os



def get_cpu_freq():
    # current, min, max
    cpu = psutil.cpu_freq()
    return cpu


def get_cpu_load(interval):
    load_list = psutil.cpu_percent(interval=interval, percpu=True)
    return load_list


def get_process_list():
    print("Getting processes")
    process_list = []
    for proc in psutil.process_iter():
        try:
            current_psutil_process = psutil.Process(proc.pid)
            with current_psutil_process.oneshot():
                temp_process_dict = {
                    "name":             current_psutil_process.name(),
                    "cpu_percent":      current_psutil_process.cpu_percent()/psutil.cpu_count(), #This one does nothing on Windows due to some psutil limitations.
                    # Check https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_percent for more info.
                    "io_counter":       current_psutil_process.io_counters(),
                    "main_memory_usage":current_psutil_process.memory_info().rss,
                    "virtual_memory_usage": current_psutil_process.memory_info().vms
                }
                if(os.name=="nt"):
                    time.sleep(0.5)
                    temp_process_dict["cpu_percent"]= current_psutil_process.cpu_percent()/psutil.cpu_count()
                print(temp_process_dict["name"],":",temp_process_dict["cpu_percent"])
                process_list.append(temp_process_dict)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return process_list

with open("sample.json", "w") as outfile:
    json.dump(get_process_list(), outfile)