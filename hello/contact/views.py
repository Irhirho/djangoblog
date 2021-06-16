from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse


from forms import ContactForm

def contact_form(request):
	return render (request, 'contact/contact_form.html')
def contact(request):
        errors=[]
        if request.method=='POST':
                if not request.POST.get('subject'):
                        errors.append("enter a subject")
                if not request.POST.get('message'):
                        errors.append("enter a ,message")
                
		if request.POST.get('email') :
			email=request.POST.get('email')
			if('@' not in email):
				errors.append("not validate email address")
			
	#assert(False)
	print errors
	if not errors:
		send_mail(request.POST.get('subject'),
				request.POST.get('message'),
				request.POST.get('email','mengqingxi89@126.com'),
				['mengqingxi89@126.com'])
		return HttpResponseRedirect('/contact/thanks')


	return render (request, 'contact/contact_form.html', {
			'errors':errors,
			'subject':request.POST.get('subject'),
			'message':request.POST.get('message'),
			'email':request.POST.get('email')})
                

def thanks(request):
	return HttpResponse("thanks")



def contactWithForm(request):

        errors=[]

	print len(errors)
        if request.method=='POST':
		form=ContactForm(request.POST)
		if form.is_valid():
			cd=form.cleaned.data
			
			send_mail(cd['subject'],
				cd['message'],
				cd.get('email','mengqingxi89@126.com'),
				['mengqingxi89@126.com'])
			return HttpResponseRedirect('/contact/thanks')


	else:
		form=ContactForm(initial={
				'subject':'my site',
				'email':'example@meng.com'})
	return render(request,'contact/contact_form.html',{'form':form})
                

def thanks(request):
	return HttpResponse("thanks")




