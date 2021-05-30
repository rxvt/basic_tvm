from django.db import models

# Create your models here.


class Command(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    document = models.JSONField(default=dict)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
