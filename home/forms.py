from django import forms
from .models import Feedback,Contact

#feedback
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name' ,'email' ,'comments']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name" ,'email','message']