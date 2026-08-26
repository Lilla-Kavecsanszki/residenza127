from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
import os
import logging
import requests

from django.conf import settings
from django.utils.translation import get_language
from django.utils.translation import gettext as _

from .forms import ContactForm
from .models import Contact
from properties.models import Property


# Configure logging
logger = logging.getLogger(__name__)


def homepage(request):
    """Fetch properties and handle contact form submissions."""
    properties = Property.objects.all()
    form = ContactForm()

    # Cloudflare Turnstile site key
    turnstile_site_key = os.environ.get("TURNSTILE_SITE_KEY")

    # Get the current active language code
    current_language = get_language()

    # Construct the canonical URL based on the active language
    canonical_url = request.build_absolute_uri(f"/{current_language}/")

    # Log the canonical URL for debugging purposes
    logger.info(f"Canonical URL: {canonical_url}")

    if request.method == "POST":
        # Get the Turnstile token generated in the browser
        turnstile_token = request.POST.get("cf-turnstile-response")

        # Verify the Turnstile token with Cloudflare
        try:
            turnstile_response = requests.post(
                "https://challenges.cloudflare.com/turnstile/v0/siteverify",
                data={
                    "secret": os.environ.get("TURNSTILE_SECRET_KEY"),
                    "response": turnstile_token,
                },
                timeout=10,
            )
            turnstile_response.raise_for_status()
            turnstile_result = turnstile_response.json()

        except (requests.RequestException, ValueError) as e:
            logger.exception("Turnstile verification request failed: %s", e)
            messages.error(
                request,
                _("Security verification is temporarily unavailable. Please try again.")
            )
            return redirect("home")

        # Stop the submission if Cloudflare did not verify the visitor
        if not turnstile_result.get("success"):
            logger.warning(
                "Turnstile verification failed. Error codes: %s",
                turnstile_result.get("error-codes", [])
            )
            messages.error(
                request,
                _("Security verification failed. Please try again.")
            )
            return redirect("home")

        # Validate the Django contact form
        form = ContactForm(request.POST)

        if form.is_valid():
            # Save the contact submission to the database
            contact_submission = Contact(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone_number=form.cleaned_data["phone_number"],
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["message"],
            )
            contact_submission.save()

            # Prepare the email to the property owner
            owner_email = EmailMultiAlternatives(
                subject=form.cleaned_data["subject"],
                body=(
                    f"Messaggio da {form.cleaned_data['name']} "
                    f"<{form.cleaned_data['email']}>\n\n"
                    f"Email: {form.cleaned_data['email']}\n\n"
                    f"Telefono: {form.cleaned_data['phone_number']}\n\n"
                    f"{form.cleaned_data['message']}"
                ),
                from_email=None,
                to=[os.environ.get("CONTACT_EMAIL_RECIPIENT")],
            )

            try:
                owner_email.send()

            except Exception as e:
                logger.exception("Failed to send contact email to owner: %s", e)
                messages.error(
                    request,
                    _("Failed to send message to the property owner.")
                )
                return redirect("home")

            # Prepare the email to the user
            user_email = EmailMultiAlternatives(
                subject="Your Contact Form Submission",
                body=(
                    f"Gentile {form.cleaned_data['name']},\n\n"
                    "Grazie per averci contattato! Apprezziamo la sua richiesta "
                    "e le risponderemo al più presto.\n\n"
                    "Nel frattempo, troverà in allegato la brochure per la sua "
                    "consultazione.\n\n"
                    "Cordiali saluti,\n"
                    "Ar.Gi. Costruzioni"
                ),
                from_email=None,
                to=[form.cleaned_data["email"]],
            )

            # Path to the brochure file
            brochure_path = os.path.join(
                settings.BASE_DIR,
                "staticfiles",
                "files",
                "brochure.pdf",
            )

            # Attach the brochure if it exists
            if os.path.exists(brochure_path):
                user_email.attach_file(brochure_path)

            # Send confirmation email to the user
            try:
                user_email.send()

                messages.success(
                    request,
                    _("Thank you for submitting! We will be in touch soon!")
                )

            except Exception as e:
                logger.exception(
                    "Failed to send confirmation email to user: %s",
                    e
                )
                messages.error(
                    request,
                    _("Failed to send the brochure to your email.")
                )
                return redirect("home")

            return redirect("home")

    context = {
        "property_list": properties,
        "form": form,
        "canonical_url": canonical_url,
        "turnstile_site_key": turnstile_site_key,
    }

    return render(request, "index.html", context)