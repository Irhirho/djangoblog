# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

import datetime

def helloWorld(request):
	return HttpResponse("hello world the fuck ")

def mytime(request):
	now=datetime.datetime.now()
#	res="<html><head>shit </head><body> what the fuck<li>%s<li><body><html>" %now
	t=get_template('curtime.html')
	res=t.render(Context({'dt':now}))
	return HttpResponse(res)
def timedealt(request,off):
	h=int(off)
	#assert False

	now=datetime.datetime.now() + datetime.timedelta(hours=h)
	res="<html><head>shit </head><body> what the fuck<li>%s<li><body><html>" %now
	return HttpResponse(res)
