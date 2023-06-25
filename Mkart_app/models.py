from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    age = models.IntegerField(null=True)

    def __str__(self) -> str:
        return self.name

class Login(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    