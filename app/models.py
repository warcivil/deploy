from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, null=True)
    comleted = models.BooleanField(default=False)
