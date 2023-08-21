from django.db import models

# Create your models here.

class Serves(models.Model):
    poster = models.ImageField(upload_to='images/',blank=True,verbose_name='Serves img')
    description = models.TextField()

    def __self__ (self):
        return f'serves of {self.description}'

class Serves_list(models.Model):
    post = models.ForeignKey(Serves, on_delete=models.SET_NULL, null=True, related_name='serveslist')
    title = models.CharField(max_length=100)

    def __str__(self):
       return f'Images of {self.post.title}'
    
class Texnologies(models.Model):
    post = models.ForeignKey(Serves, on_delete=models.SET_NULL, null=True, related_name='texnologies')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
       return f'Images of {self.post.name}'

class Developers(models.Model):
    post = models.ForeignKey(Serves, on_delete=models.SET_NULL, null=True, related_name='developers')
    dev_name = models.CharField(max_length=100)
    dev_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
       return f'Images of {self.dev_name}'
