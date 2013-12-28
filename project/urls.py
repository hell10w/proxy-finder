from django.conf.urls import patterns, include, url
from django.contrib import admin; admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^rosetta/', include('rosetta.urls')),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    url(r'^api/', include('proxyfinder.restapi')),
    url(r'^', include('proxyfinder.urls', namespace='proxyfinder')),

)
