import datetime

import psutil
import time
import os
import json


class Pyrocess:  # Not setting the class name to "Process"

    def __init__(self, pid, name, cpu, io_counter, memory, vmemory):
        self.pid = pid
        self.name = name
        self.cpu = cpu
        self.io_counter = io_counter,
        self.memory = memory,
        self.virtual_memory = vmemory


class Timestap:

    def __init__(self, interval_cpu_load_calculation):
        self.captured_time = datetime.time
        # General stats
        self.cpu_freq = psutil.cpu_freq()
        self.cpu_load_list = psutil.cpu_percent(interval=interval_cpu_load_calculation, percpu=True)
        self.processes = []

    def add_process_to_timestamp(self, process):
        self.processes.append(process)

    def get_all_process(self):
        print("Getting processes")
        temp_processes = [psutil.Process(proc.pid) for proc in psutil.process_iter()]
        process_list = []
        for current_psutil_process in temp_processes:
            try:
                with current_psutil_process.oneshot():
                    current_psutil_process.cpu_percent()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        time.sleep(0.5)
        for current_psutil_process in temp_processes:
            try:
                with current_psutil_process.oneshot():
                    self.processes.append(Pyrocess(current_psutil_process.pid, current_psutil_process.name(),
                                                   (current_psutil_process.cpu_percent() / psutil.cpu_count()),
                                                   current_psutil_process.io_counters(),
                                                   current_psutil_process.memory_info().rss,
                                                   current_psutil_process.memory_info().vms))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        self.processes.sort(key=lambda x: x['cpu_percent'], reverse=True)

