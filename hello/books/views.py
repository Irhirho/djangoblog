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

def index(request):
        alist=[]
        alist.append(request.path)
        alist.append(request.get_host())
        alist.append(request.get_full_path())
        alist.append(request.is_secure())
        #alist.append(request.META['HTTP_REFERER'])
        #alist.append(request.META['HTTP_USER_AGENT'])
        #alist.append(request.META['REMOTE_ADDR'])
        alist.append(request.META.get('HTTP_REFERER'))
        alist.append(request.META.get('HTTP_USER_AGENT'))
        alist.append(request.META.get('REMOTE_ADDR'))
	return (render(request,'books/curdata.html',{'datalist':alist}))


       
def search(request):
        return (render(request,'books/search.html'))

def searchbus(request):
       
        error='0'
        if 'q' in request.GET and request.GET['q']:
                q=request.GET['q']
                authors = Author.objects.filter(first_name__contains=q)
                #alist=Author.objects.filter(first_name_contains="ah")
                if len(authors)==0:
                        
                        return (render(request,'books/search.html',{'error':'2'}))
                return (render (request, 'books/search_result.html',{'authors':authors,'query':q}))
        else:
                if 'q' in request.GET and not request.GET['q']:
                        error='3'
                #message="you must input a keyword to search"
#                return HttpResponse('error')
                return (render(request,'books/search.html',{'error':error}))



