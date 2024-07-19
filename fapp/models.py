from django.db import models

# Create your models here.

class ToDo(models.Model):

    Task = models.CharField(max_length= 250)
    Date = models.DateField()
    Time = models.TimeField()

    # def __str__(self):
    #     return self.Name
