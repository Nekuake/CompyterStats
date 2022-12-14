from datetime import datetime
import socket, psutil, time, netifaces, re, uuid


class Pyrocess:  # Not setting the class name to "Process"

    def __init__(self, pid, name, cpu, io_counter, memory, vmemory):
        self.pid = pid
        self.name = name
        self.cpu = cpu
        self.io_counter = io_counter,
        self.memory = memory,
        self.virtual_memory = vmemory


class Timestamp:

    def __init__(self):
        self.captured_time = str(datetime.now())
        # General stats
        self.cpu_freq = psutil.cpu_freq().current
        self.cpu_load_list = psutil.cpu_percent(interval=0.5)
        self.vmemory_capacity = psutil.virtual_memory().available >> 20
        self.vmemory_usage = psutil.virtual_memory().total >> 20
        self.storage_free = psutil.disk_usage("C://").free >> 20
        self.storage_total = psutil.disk_usage("C://").total >> 20
        self.processes = []
        # Get all processes
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
                    self.processes.append(Pyrocess(current_psutil_process.pid,
                                        current_psutil_process.name(),
                                        (current_psutil_process.cpu_percent() / psutil.cpu_count()),
                                        current_psutil_process.io_counters().read_count,
                                        current_psutil_process.memory_info().rss,
                                        current_psutil_process.memory_info().vms))
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        # self.processes.sort(key=lambda x: x['cpu_percent'], reverse=True)


class Computer:

    def __init__(self):

        #Using main MAC address as ID. Not a perfect solution yet
        self.id= (':'.join(re.findall('..', '%012x' % uuid.getnode())))
        self.name = socket.gethostname()
        self.timestamps = {}

    def add_timestamp(self):
        new_timestamp = Timestamp()
        self.timestamps[str(datetime.now())] = new_timestamp
        return new_timestamp
