# Create your views here.
from models import Author
from django.http import HttpResponse
from django.shortcuts import render

def createmy(resquest):
	print 'meng'
	a=Author(first_name="ahrca",last_name="bbb")
	a.save()
	return HttpResponse("yes")

def disdata(request):
	print 'dis'
	#alist=Author.objects.all()
	alist=Author.objects.filter(first_name__contains="ah")
	#alist=Author.objects.get(last_name="bbb")
#	return HttpResponse(alist)
	#t=get_template('books/curdata.html')
	#t.render()
	return (render(request,'books/curdata.html',{'datalist':alist}))

def updatedata(request,target,namenew):
	print target
	print Author.objects.filter(first_name=target).update(last_name=namenew)
	alist=Author.objects.all()
	return (render(request,'books/curdata.html',{'datalist':alist}))
