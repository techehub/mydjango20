from django import forms


class ContactUsForm (forms.Form):
   name = forms.CharField(label='Your name', max_length=100)
   phone = forms.CharField(label='Your Phone', max_length=100)
   email = forms.EmailField(label='Your email', max_length=100)
   message = forms.CharField(widget=forms.Textarea(attrs={'width': "100%", 'cols': "80", 'rows': "20", }))
