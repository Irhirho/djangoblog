from django.db import models
from django.contrib import admin

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=32)
  def __unicode__(self):
    return self.name
  class Admin:
    pass


class Article(models.Model):
  title         = models.CharField(max_length=64)
  published_at  = models.DateTimeField('date published')
  content       = models.TextField()
  category      = models.ForeignKey(Category)
  def __unicode__(self):
    return self.title
  class Admin:
    pass
    
admin.site.register(Category)
admin.site.register(Article) 
