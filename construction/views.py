from django.shortcuts import render

def construction(request):
    # Set your canonical URL here
    canonical_url = 'https://www.argicostruzioni.com//construction/'  # Update with your actual URL
    return render(request, "construction/construction.html", {
        'canonical_url': canonical_url  # Pass the canonical URL to the template
    })
