from django import forms
from .models import Contact




class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name',
                  'subject',
                  'phone',
                  'email',
                  'message',
                  )