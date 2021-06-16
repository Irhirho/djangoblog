from django.conf.urls.defaults import *
from models import Author

urlpatterns=patterns('',
		(r'^create$','books.views.createmy'),
		(r'^dis$','books.views.disdata'),
		(r'^update/([a-zA-Z]*)/([a-zA-Z]+)$','books.views.updatedata'),
	#	(r'^search$','books.views.search'),
		(r'^searchbus/$','books.views.searchbus'),
		(r'^$','books.views.index'),
		)
