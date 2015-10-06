from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/', include('UserInfo.urls')),
    url(r'^secure/', include('Secure.urls')),
    url(r'^', include('PubSite.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
