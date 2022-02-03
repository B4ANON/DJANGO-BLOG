from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from .helper import*




class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000,null=True)
    
    def __str__(self):
        return self.title

class Posts(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=20, null=True)
    dishname = models.CharField(max_length=50, null=True)
    averageprice = models.IntegerField(null=True)
    content = RichTextField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="Post/imgs")
    created_at = models.DateTimeField(auto_now_add=True)
    upload_at = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.title + ' by ' + self.author

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Posts,self).save(*args, **kwargs)


class Comment(models.Model):
    comid = models.ForeignKey(Posts,on_delete=models.CASCADE,null=True,related_name='commen')
    commname = models.CharField(max_length=10)
    commsec = models.CharField(max_length=50)
    comdate = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return '%s - %s' % (self.comid, self.commname)