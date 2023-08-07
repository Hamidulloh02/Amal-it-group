from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Portfolio (models.Model):
    title = models.CharField(max_length=100)
    subinfo =  RichTextField()
    poster = models.ImageField(upload_to='images/',blank=True,verbose_name='Products upload image')
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
