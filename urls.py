from django.conf.urls.defaults import patterns, include, url
from frontend.views import listing, details
from django.contrib import admin
import settings
from frontend.feeds import LatestEntriesFeed

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$',  listing),
    (r'^details/$',  details),
    (r'^(?P<path>.*\.(js|css|xls|ico|png|gif|jpg|jpeg|doc|xpi|rdf|exe|swf|msi|crx|xml|mp3|htm))$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^feed/$', LatestEntriesFeed()),

)
