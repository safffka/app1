from django.db import models

def upload_to(instance,filename):
    return 'images/{filename}'.format(filename=filename)


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    file_1 = models.ContentTypeRestrictedFileField(upload_to=upload_to,content_types=['video/mov', 'video/mp4', 'image/jpg','image/png'],max_upload_size=214958080,  null=True,blank=True)
    file_2 = models.ContentTypeRestrictedFileField(upload_to=upload_to,content_types=['video/mov', 'video/mp4', 'image/jpg','image/png'],max_upload_size=214958080,  null=True,blank=True)
    file_3 = models.ContentTypeRestrictedFileField(upload_to=upload_to,content_types=['video/mov', 'video/mp4', 'image/jpg','image/png'],max_upload_size=214958080,  null=True,blank=True)
    file_4 = models.ContentTypeRestrictedFileField(upload_to=upload_to,content_types=['video/mov', 'video/mp4', 'image/jpg','image/png'],max_upload_size=214958080,  null=True,blank=True)
    file_5 = models.ContentTypeRestrictedFileField(upload_to=upload_to,content_types=['video/mov', 'video/mp4', 'image/jpg','image/png'],max_upload_size=214958080,  null=True,blank=True)
    class Meta:
        ordering = ['created']


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    image = models.FileField(upload_to='images/')


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'

# Create your models here.
