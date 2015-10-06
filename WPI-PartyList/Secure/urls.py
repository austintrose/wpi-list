from django.conf.urls import patterns, include, url

from Secure import views

urlpatterns = patterns('',
	url(r'^$', 'Secure.views.index'),
    url(r'^parties/', include('PartyList.urls')),
    url(r'^users/', include('UserInfo.secure_urls')),
)



