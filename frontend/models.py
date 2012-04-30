from django.db import models
from django.contrib import admin
from django.conf.global_settings import MEDIA_ROOT

class Categories(models.Model):
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

class Record(models.Model):
    title = models.CharField(max_length=200)
    cut = models.TextField()
    text = models.TextField()
    category = models.ForeignKey(Categories)
    published = models.BooleanField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

class RecordAdmin(admin.ModelAdmin):
	class Media:
		js = (MEDIA_ROOT+'/js/tiny_mce/tiny_mce.js',
                MEDIA_ROOT+'/js/textareas.js')


admin.site.register(Record, RecordAdmin)
admin.site.register(Categories)