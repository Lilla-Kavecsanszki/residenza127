from django import forms
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from .models import Contact

class ContactForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': _('e.g., +39 333 123 4567')})
    )

    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': _('John Doe')}),
            "email": forms.EmailInput(attrs={'placeholder': _('example.site.com')}),
            "subject": forms.TextInput(attrs={'placeholder': _('What would you like to discuss?')}),
            "message": forms.Textarea(attrs={'rows': 4, 'placeholder': _('Your Message')}),
        }