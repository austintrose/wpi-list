from django.conf.urls import patterns, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(pattern_name='PartyList.views.index'), name='parties'),
	url(r'^all/$', 'PartyList.views.index'),
	url(r'^add/$', 'PartyList.views.add_party'),
	url(r'^manage/$', 'PartyList.views.manage_parties', name='manage_parties'),
	url(r'^edit/(?P<party>[\d]+)/$', 'PartyList.views.edit_party'),
	url(r'^delete/(?P<party>[\d]+)/$', 'PartyList.views.delete_party'),
	url(r'^view/(?P<party>[\d]+)/guests/$', 'PartyList.views.guests'),
	url(r'^view/(?P<party>[\d]+)/guests/create/$', 'PartyList.api.create'),
	url(r'^view/(?P<party>[\d]+)/guests/destroy/(?P<guestID>[\d]+)/$', 'PartyList.api.destroy'),
	url(r'^view/(?P<party>[\d]+)/guests/signIn/(?P<guestID>[\d]+)/$', 'PartyList.api.signin'),
	url(r'^view/(?P<party>[\d]+)/guests/signOut/(?P<guestID>[\d]+)/$', 'PartyList.api.signout'),
	url(r'^view/(?P<party>[\d]+)/guests/poll/$', 'PartyList.api.poll'),
	url(r'^view/(?P<party>[\d]+)/guests/export/$', 'PartyList.api.export_list'),
	url(r'^view/(?P<party>[\d]+)/guests/count/$', 'PartyList.api.updateCount'),
	url(r'^view/(?P<party>[\d]+)/guests/count/poll/$', 'PartyList.api.pollCount'),
	url(r'^view/(?P<party>[\d]+)/guests/init/$', 'PartyList.api.initPulse'),
)
