from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Computer(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Timestamp(models.Model):
    datetime_captured = models.DateTimeField('date captured', primary_key=True)
    avg_cpu_usage=models.FloatField('overall cpu usage')
    virtual_memory_usage=models.FloatField('overall memory usage')
    virtual_memory_capacity=models.FloatField('max memory capacity')
    disk_usage=models.FloatField('disk usage')
    disk_capacity=models.FloatField('disk capacity')
    computer=models.ForeignKey('computer', on_delete=models.CASCADE)


class Process(models.Model):
    timestamp=models.ForeignKey('Timestamp', on_delete=models.CASCADE)
    captured_timestamp = models.ForeignKey(Timestamp, on_delete=models.CASCADE)
    pid=models.IntegerField('process id')
    cpu_usage=models.FloatField('cpu usage per process')
    name=models.CharField(max_length=200)
    io_counter=models.CharField(max_lenght=200)
    memory_data=models.FloatField()
    virtual_memory_data=models.FloatField()

    
