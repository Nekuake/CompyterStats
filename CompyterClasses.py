import datetime

import psutil
import time
import os

class Process:

    def __init__(self, pid):
        self.pid=pid


class Timestap:

    def __init__(self, interval_cpu_load_calculation):
        captured_time=datetime.time
        #General stats
        cpu_freq=psutil.cpu_freq()
        cpu_load_list=psutil.cpu_percent(interval=interval_cpu_load_calculation, percpu=True)
        processes=[]

    def add_process_to_timestamp(self, process):
        self.processes.append(process)








def get_cpu_load(interval):
    load_list = psutil.cpu_percent(interval=interval, percpu=True)
    return load_list


def get_process_list():
    print("Getting processes")
    process_list = []
    if os.name == "nt":
        for proc in psutil.process_iter():
            try:
                current_psutil_process = psutil.Process(proc.pid)
                with current_psutil_process.oneshot():
                    current_psutil_process.cpu_percent() / psutil.cpu_count()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        time.sleep(0.5)
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
                print(temp_process_dict["name"],":",temp_process_dict["cpu_percent"])
                process_list.append(temp_process_dict)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return process_list

with open("sample.json", "w") as outfile:
    json.dump(get_process_list(), outfile)

