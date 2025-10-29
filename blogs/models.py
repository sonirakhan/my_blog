from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (('DRAFT','Draft'),('PUBLISHED','Published'))
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(unique=True,max_length=250,blank=True)
    # unique=True ensures no duplicate slugs
    # blank=True allows the slug to be empty initially, before saving
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30,choices=STATUS_CHOICES,default='DRAFT')


    class Meta:
        ordering = ['-created']


    def save(self,*args, **kwargs):
        if not self.slug:  # Only generate if slug is not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.name}'
