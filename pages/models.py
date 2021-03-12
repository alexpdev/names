from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    sex = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return self.name
