from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    names = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)

    def __str__ (self):
        return self.names