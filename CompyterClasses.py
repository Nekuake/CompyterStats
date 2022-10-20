import datetime

import psutil
import time
import os
import json


class Process:

    def __init__(self, pid):
        self.pid=pid


class Timestap:

    def __init__(self, interval_cpu_load_calculation):
        self.captured_time=datetime.time
        #General stats
        self.cpu_freq=psutil.cpu_freq()
        self.cpu_load_list=psutil.cpu_percent(interval=interval_cpu_load_calculation, percpu=True)
        self.processes=[]

    def add_process_to_timestamp(self, process):
        self.processes.append(process)

    def get_all_process(self):
        print("Getting processes")
        process_list = []
        for proc in psutil.process_iter():
            try:
                current_psutil_process = psutil.Process(proc.pid)
                with current_psutil_process.oneshot():
                    temp_process_dict = {
                        "name": current_psutil_process.name(),
                        "cpu_percent": current_psutil_process.cpu_percent() / psutil.cpu_count(),
                        # This one does nothing on Windows due to some psutil limitations.
                        # Check https://psutil.readthedocs.io/en/latest/#psutil.Process.cpu_percent for more info.
                        "io_counter": current_psutil_process.io_counters(),
                        "main_memory_usage": current_psutil_process.memory_info().rss,
                        "virtual_memory_usage": current_psutil_process.memory_info().vms
                    }
                    print(temp_process_dict["name"], ":", temp_process_dict["cpu_percent"])
                    process_list.append(temp_process_dict)
                    self.add_processes_to_timestamp(self,temp_process_dict)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue






