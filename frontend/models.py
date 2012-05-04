from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.conf.global_settings import MEDIA_ROOT

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

class Record(models.Model):
    title = models.CharField(max_length=200)
    cut = models.TextField()
    text = models.TextField()
    category = models.ForeignKey(Category)
    published = models.BooleanField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

class RecordAdmin(admin.ModelAdmin):
	class Media:
		js = (MEDIA_ROOT+'/js/tiny_mce/tiny_mce.js',
                MEDIA_ROOT+'/js/textareas.js')

class BlogSetting(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    header_title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    description = models.TextField()


admin.site.register(Record, RecordAdmin)
admin.site.register(Category)
admin.site.register(BlogSetting)