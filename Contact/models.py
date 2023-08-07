from django.db import models

# Create your models here.


class Contact(models.Model):
    surname = models.CharField( null=False, max_length=100)
    phonenumber = models.CharField(null=False,max_length=100)
    text = models.TextField()

    def __self__(self):
        return self.surname