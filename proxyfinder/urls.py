from django.conf.urls import url, patterns, include
from django.views.generic import TemplateView

from views import ProxiesListView


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    #url(r'^api/', include(router.urls)),
    url(r'^$',
        TemplateView.as_view(template_name='proxyfinder/about.html'),
        name='about'),
    url(r'^proxylist$', ProxiesListView.as_view(), name='proxylist'),
)
