from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
import os
import logging
from django.conf import settings
from .forms import ContactForm
from django.utils.translation import get_language
from django.utils.translation import gettext as _
from .models import Contact
from properties.models import Property

# Configure logging
logger = logging.getLogger(__name__)

def homepage(request):
    """Fetch properties and handle contact form submissions."""
    properties = Property.objects.all()  # Fetch all properties
    form = ContactForm()  # Initialize the contact form
    
    # Get the current active language code
    current_language = get_language()  # e.g., 'it' or 'en'

    # Construct the canonical URL based on the active language
    canonical_url = request.build_absolute_uri(f"/{current_language}/")  # e.g., /en/ or /it/

    # Log the canonical URL for debugging purposes
    logger.info(f"Canonical URL: {canonical_url}")

    if request.method == "POST":
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
                from_email=None,  # Default from email
                to=[os.environ.get("CONTACT_EMAIL_RECIPIENT")],
            )
            try:
                owner_email.send()
            except Exception as e:
                messages.error(request, _("Failed to send message to the property owner."))
                return redirect("home")  # Redirect to the homepage if email fails

            # Prepare the email to the user
            user_email = EmailMultiAlternatives(
                subject="Your Contact Form Submission",
                body=(
                    f"Gentile {form.cleaned_data['name']},\n\n"
                    "Grazie per averci contattato! Apprezziamo la sua richiesta e le risponderemo al più presto.\n\n"
                    "Nel frattempo, troverà in allegato la brochure per la sua consultazione.\n\n"
                    "Cordiali saluti,\n"
                    "Ar.Gi. Costruzioni"
                ),
                from_email=None,  # Default from email
                to=[form.cleaned_data['email']],
            )

            # Path to the brochure file
            brochure_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'files', 'brochure.pdf')
            # Check if the brochure file exists before attaching it
            if os.path.exists(brochure_path):
                user_email.attach_file(brochure_path)  # Attach the PDF

            # Send the email to the user
            try:
                user_email.send()
                messages.success(request, _("Thank you for submitting! We will be in touch soon!"))
            except Exception as e:
                messages.error(request, _("Failed to send the brochure to your email."))
                return redirect("home")  # Redirect to the homepage if email fails

            return redirect("home")  # Redirect to the homepage after successful submission

    context = {
        "property_list": properties,  # Pass properties to the template
        "form": form,  # Pass the contact form to the template
        "canonical_url": canonical_url,  # Pass the canonical URL to the template
    }

    return render(request, "index.html", context)  # Render the homepage template