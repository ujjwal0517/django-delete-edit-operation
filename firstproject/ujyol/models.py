from django.db import models

class position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contactno = models.CharField(max_length=50)
    position = models.ForeignKey(position, on_delete=models.CASCADE)

# Create your models here.


