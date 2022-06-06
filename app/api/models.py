from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now

from decimal import Decimal

from django.db import models


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    file_1 = models.ImageField(upload_to=upload_to, null=True, blank=True)
    street = models.CharField(max_length=100, blank=True, default='')
    altitude = models.DecimalField(max_digits=100, decimal_places=20, default=0.0)
    longitude = models.DecimalField(max_digits=100, decimal_places=20, default=0.0)
    date = models.DateTimeField(blank=True, default=now)

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)

    class Meta:
        ordering = ['created']


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'


class User(models.Model):
    email = models.EmailField(unique=True, blank=True)
    ava = models.ImageField(upload_to=upload_to, null=True, blank=True)
    password=models.CharField(blank=True,max_length=100)
    username=models.CharField(unique=True,blank=True,max_length=100)

