import json
import logging
import psutil
import time
import os


# psutil uses named tuples for the most of their functions and data.
# For consistency and clarity, this project aims to use the same data container type.


def get_cpu_freq():
    # current, min, max
    logging.info("Getting CPU freq")
    cpu = psutil.cpu_freq()
    return cpu


def get_cpu_load(interval):
    logging.info("Getting CPU load per core")
    load_list = psutil.cpu_percent(interval=interval, percpu=True)
    return load_list


# Windows needs a specific way to calculate CPU usage.
# Check https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_percent for more info.

def get_disk_usage(perdisk):
    disk_usage = psutil.disk_io_counters(perdisk=perdisk)
    if disk_usage == None or disk_usage == {}:
        raise Warning(
            "Disk Usage returned None. Diskless system? If not and you are on Windows, try running diskperf -y  Returning 0")
        disk_usage = 0
    return disk_usage


def get_process_list(cpu_interval_secs):
    logging.info("Getting process list.")
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
                    "pid": current_psutil_process.pid,
                    "name": current_psutil_process.name(),
                    "cpu_percent": current_psutil_process.cpu_percent(interval=cpu_interval_secs) / psutil.cpu_count(),
                    "io_counter": current_psutil_process.io_counters(),
                    "main_memory_usage": current_psutil_process.memory_info().rss,
                    "virtual_memory_usage": current_psutil_process.memory_info().vms
                }
                if(os.name=="nt"):
                    time.sleep(0.5)
                    temp_process_dict["cpu_percent"]= current_psutil_process.cpu_percent()/psutil.cpu_count()
                print(temp_process_dict["name"],":",temp_process_dict["cpu_percent"])
                process_list.append(temp_process_dict)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    if os.name == "nt":
        time.sleep(1)
        for process in process_list:
            process["cpu_percent"] = psutil.Process(process["pid"]).cpu_percent() / psutil.cpu_count()
    return process_list


def get_boot_time():
    return psutil.boot_time()


with open("sample.json", "w") as outfile:
    json.dump(get_process_list(0.1), outfile)
    json.dump(get_process_list(0.1), outfile)