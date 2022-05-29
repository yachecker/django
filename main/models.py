from tabnanny import verbose
from django.db import models


class Task(models.Model):
    title = models.CharField('Task name', max_length=50)
    description = models.TextField('Description', max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
