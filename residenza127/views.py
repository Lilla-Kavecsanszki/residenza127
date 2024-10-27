import logging

from django.shortcuts import redirect, render
from django.utils import translation
from django.http import HttpResponse

# Configure logging
logger = logging.getLogger(__name__)


def handler404(request, exception):
    """Error Handler 404 - Page Not Found"""
    return render(request, "errors/404.html", status=404)


def language_switch(request, lang_code):
    # Set the language
    translation.activate(lang_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code

    # Redirect to the previous page
    return redirect(request.META.get("HTTP_REFERER", "/"))


# Dynamic robots_txt file generaction
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /accounts/",
        "Disallow: /profiles/",
        "Sitemap: https://www.argicostruzioni.com/sitemap.xml",  # Custom domain
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
