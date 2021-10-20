from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.fields import SlugField
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name 


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100 , null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)


    def __str__(self):
        return self.name



class Project(models.Model):
    category = models.ManyToManyField('Category', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)                                 
    date_created = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    photo = models.ImageField(upload_to='image_project', null=True, blank=True)



    def __str__(self):

        return self.title 

