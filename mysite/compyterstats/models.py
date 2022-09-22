from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Computer(models.Model):
    name = models.CharField(max_length=200)
    private_ip=models. CharField(max_length=20)
    date_added = models.DateTimeField('date added')
    def __str__(self):
        return self.name

class Timestamp(models.Model):
    origin_computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    datetime_captured = models.DateTimeField('date captured', primary_key=True)
    avg_cpu_usage=models.FloatField('overall cpu usage')
    virtual_memory_usage=models.FloatField('overall memory usage')
    virtual_memory_capacity=models.FloatField('max memory capacity')
    disk_usage=models.FloatField('disk usage')
    disk_capacity=models.FloatField('disk capacity')

class Process(models.Model):
    captured_timestamp = models.ForeignKey(Timestamp, on_delete=models.CASCADE)
    pid=models.IntegerField('process id', primary_key=True)
    cpu_usage=models.FloatField('cpu usage per process')
    
