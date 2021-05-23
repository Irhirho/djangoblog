from django.conf.urls.defaults import *
from models import Article

info_dict = {
'queryset': Article.objects.all(),
}

#urlpatterns = patterns('',
#(r'^$', 'django.views.generic.list_detail.object_list', info_dict),
#(r'^(?Pd+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
#)


urlpatterns = patterns('',
		    
	(r'^$','blog.views.mytime'),
	(r'^plus/(\d{1,2})/$','blog.views.timedealt'),
	(r'^hello$','blog.views.helloWorld'),

	(r'^$', 'django.views.generic.list_detail.object_list', info_dict),
	    
	(r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
	)
