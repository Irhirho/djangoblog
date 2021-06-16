from django import forms

class ContactForm(forms.Form):
	subject =forms.CharField()
	email=forms.EmailField(required=False,label='your email address')
	message=forms.CharField(widget=forms.Textarea)

	def clean_message(self):
		mess=self.cleaned_data['message']
		num_words=len(mess.split())
		if num_words<5:
			raise forms.ValidationError("not encough words for message")
		return mess

