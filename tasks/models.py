from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class task(models.Model):
    title = models.CharField(max_length=100, verbose_name="titulo")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "tarea"
        verbose_name_plural = "tareas"

    def __str__(self):
        return self.title



