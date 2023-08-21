from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


    
class Portfolio (models.Model):
    title = models.CharField(max_length=100)
    subinfo =  RichTextField()
    poster = models.ImageField(upload_to='images/',blank=True,verbose_name='Portfolio upload image')
    # Images = models.ForeignKey(image,on_delete=models.SET_NULL, null=True,verbose_name="Category")
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class Image(models.Model):
    post = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, null=True, related_name='images')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
       return f'Images of {self.post.id}'


