import logging
from allauth.account.adapter import DefaultAccountAdapter
from django.utils import translation
from django.urls import reverse

class MyAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailaddress):
        # Get the current language
        current_language = translation.get_language()

        # Build the absolute URL for email confirmation with the current language
        confirmation_url = request.build_absolute_uri(
            reverse('account_confirm_email', args=[emailaddress.key])
        )
        
        # Append the language parameter to the URL
        return f"{confirmation_url}?lang={current_language}"
