from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    url(r'^$', 'Secure.views.index'),
    url(r'^login', 'django.contrib.auth.views.login'),
    url(r'^logout', 'django.contrib.auth.views.logout_then_login'),
    url(r'^403/', 'PubSite.views.permission_denied'),
)