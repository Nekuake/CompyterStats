import json
import logging
import psutil
import time
import os



def get_cpu_freq():
    # current, min, max
    logging.info("Getting CPU freq")
    cpu = psutil.cpu_freq()
    return cpu


def get_cpu_load(interval):
    logging.info("Getting CPU load per core")
    load_list = psutil.cpu_percent(interval=interval, percpu=True)
    return load_list

#Windows needs a specific way to calculate CPU usage.
# Check https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_percent for more info.

def get_disk_usage(perdisk):
    disk_usage=psutil.disk_io_counters(perdisk=perdisk)
    if disk_usage== None or disk_usage=={}:
        raise Warning("Disk Usage returned None. Diskless system? Returning 0")
        disk_usage=0
    return disk_usage


def get_process_list():
    logging.info("Getting process list.")
    process_list = []
    for proc in psutil.process_iter():
        try:
            current_psutil_process = psutil.Process(proc.pid)
            with current_psutil_process.oneshot():
                temp_process_dict = {
                    "name":             current_psutil_process.name(),
                    "cpu_percent":      current_psutil_process.cpu_percent()/psutil.cpu_count(),
                    "io_counter":       current_psutil_process.io_counters(),
                    "main_memory_usage":current_psutil_process.memory_info().rss,
                    "virtual_memory_usage": current_psutil_process.memory_info().vms
                }
                print(temp_process_dict["name"],":",temp_process_dict["cpu_percent"])
                process_list.append(temp_process_dict)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return process_list

