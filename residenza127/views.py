from django.shortcuts import redirect
from django.utils import translation
from django.conf import settings
import logging

# Configure logging
logger = logging.getLogger(__name__)

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)

def language_switch(request, lang_code):
    """ Switch the language and redirect back to the referring page """
    if lang_code in dict(settings.LANGUAGES):
        logger.debug(f"Switching language to: {lang_code}")
        # Set the language in the session
        request.session['django_language'] = lang_code
        translation.activate(lang_code)
        response = redirect(request.META.get('HTTP_REFERER', '/'))
        return response
    else:
        logger.warning(f"Attempted to switch to invalid language: {lang_code}")
        return redirect('/')
