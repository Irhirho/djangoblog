from django.conf.urls.defaults import *
from models import Author

urlpatterns=patterns('',
		(r'^create$','books.views.createmy'),
		(r'^dis$','books.views.disdata'),
		(r'^update/([a-zA-Z]*)/([a-zA-Z]+)$','books.views.updatedata'),
		)
