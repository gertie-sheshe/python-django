from django.db import models

# Create your models here.

class ToDo(models.Model):
    complete = models.BooleanField(default = False)
    todoTask = models.CharField(max_length = 50)

    def __str__(self):
        return self.todoTask
