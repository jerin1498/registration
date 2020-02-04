from django.db import models

# Create your models here.


class Time(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    current_time = models.DateTimeField(auto_now_add=True)
    set_time = models.DateTimeField()
