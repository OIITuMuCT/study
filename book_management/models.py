from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=225)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.name, self.author
