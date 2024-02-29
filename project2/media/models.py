from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=20)

    def __str__(self):
        return self.name