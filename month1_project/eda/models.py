from django.db import models


# Create your models here.
class NetflixData(models.Model):
    def __str__(self):
        return self.title

    type = models.CharField(max_length=15)
    title = models.CharField(max_length=50)