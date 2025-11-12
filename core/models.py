from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.name