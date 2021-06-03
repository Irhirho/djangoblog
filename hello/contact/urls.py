from django.conf.urls.defaults import *

urlpatterns=patterns('',
		(r'^contact/$','contact.views.contactWithForm'),
		(r'^thanks$','contact.views.thanks'),
		(r'^$','contact.views.contact_form'),
		)
