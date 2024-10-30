from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.functions import Lower
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from profiles.models import UserProfile

from .decorators import superuser_required
from .forms import PropertyForm, PropertyImageFormSet, PropertyVideoFormSet
from .models import Property, PropertyImage, PropertyVideo


@login_required
def like_property(request, property_id):
    """Handle like/unlike of a property."""
    property = get_object_or_404(Property, id=property_id)
    user = request.user

    if request.method == "POST":
        # Get or create the user's profile
        user_profile, created = UserProfile.objects.get_or_create(user=user)

        if user in property.liked_by.all():
            # Unlike the property
            property.liked_by.remove(user)
            user_profile.liked_properties.remove(property)
            messages.success(request, _("You have removed the apartment successfully!"))
        else:
            # Like the property
            property.liked_by.add(user)
            user_profile.liked_properties.add(property)
            messages.success(request, _("You have saved the apartment successfully.!"))

        # Redirect back to the referring page or home if not available
        return redirect(request.META.get("HTTP_REFERER", reverse("home")))
    else:
        # If not POST, just redirect to home or handle error
        return redirect(reverse("home"))


class AllProperties(View):
    def get(self, request, *args, **kwargs):
        """A view to show all properties, including sorting and search queries."""
        properties = Property.objects.all()
        query = request.GET.get("q", "")
        locations = request.GET.getlist("location")
        property_types = request.GET.getlist("type")
        sort = request.GET.get("sort", "created_at")  # Default sorting field
        direction = request.GET.get("direction", "asc")  # Default sorting direction

        # Handle sorting
        valid_sort_keys = [
            "name",
            "location",
            "property_type",
            "size",
            "created_at",
        ]
        if sort in valid_sort_keys:
            if sort == "name":
                properties = properties.annotate(lower_name=Lower("name"))
                sortkey = "lower_name"
            else:
                sortkey = sort

            if direction == "desc":
                sortkey = f"-{sortkey}"

            properties = properties.order_by(sortkey)
        else:
            messages.error(request, _("Invalid sort option selected."))

        # Handle filtering by location
        if locations:
            filtered_locations = [
                loc for loc in locations if loc
            ]  # Remove empty values
            if filtered_locations:
                properties = properties.filter(location__in=filtered_locations)

        # Handle filtering by property type
        if property_types:
            filtered_property_types = [
                ptype for ptype in property_types if ptype
            ]  # Remove empty values
            if filtered_property_types:
                properties = properties.filter(
                    property_type__in=filtered_property_types
                )

        # Handle search query
        if query:
            query = query.strip()  # Trim leading and trailing whitespace
            words = query.split()  # Split the query into individual words to allow searching for each one
            
            # Initialize an empty Q object to hold our queries
            queries = Q()
            
            # Construct queries for each word across multiple fields
            for word in words:
                queries |= (
                    Q(name__icontains=word) | 
                    Q(features__icontains=word) | 
                    Q(location__icontains=word) | 
                    Q(property_type__icontains=word)
                )
            
            # Filter properties based on the constructed queries
            properties = Property.objects.filter(queries)

        # Get distinct choices for filters
        location_choices = Property.LOCATIONS
        property_types_choices = Property.PROPERTY_TYPES

        # Prepare current sorting key
        current_sorting = f"{sort}_{direction}"
        
        # Construct the canonical URL for the properties listing
        canonical_url = request.build_absolute_uri(reverse("all_properties"))

        context = {
            "properties": properties,
            "search_query": query,
            "current_locations": locations,
            "current_property_types": property_types,
            "current_sorting": current_sorting,
            "location_choices": location_choices,
            "property_types_choices": property_types_choices,
            "canonical_url": canonical_url,
        }

        return render(request, "properties/properties.html", context)


class PropertyDetail(View):
    def get(self, request, property_id, *args, **kwargs):
        """A view to show individual property details."""
        property = get_object_or_404(Property, pk=property_id)
        liked = (
            request.user.is_authenticated
            and property.liked_by.filter(id=request.user.id).exists()
        )
        
        # Construct the canonical URL for the property detail
        canonical_url = request.build_absolute_uri(property.get_absolute_url())

        context = {
            "property": property,
            "images": property.images.all(),  # Fetch related images
            "videos": property.videos.all(),  # Fetch related videos
            "liked": liked,
            "canonical_url": canonical_url,
        }
        return render(request, "properties/property_details.html", context)


@login_required
@superuser_required
def property_management(request):
    if request.method == "POST":
        property_form = PropertyForm(request.POST, request.FILES)
        image_formset = PropertyImageFormSet(request.POST, request.FILES)
        video_formset = PropertyVideoFormSet(request.POST, request.FILES)

        if (
            property_form.is_valid()
            and image_formset.is_valid()
            and video_formset.is_valid()
        ):
            property = property_form.save()
            image_formset.instance = property
            video_formset.instance = property
            image_formset.save()
            video_formset.save()
            messages.success(request, _("Property has been successfully saved!"))
            return redirect(
                "all_properties"
            )  # Ensure this matches the URL pattern name
        else:
            messages.error(
                request,
                _("There was an error saving the property. Please check the form for errors.",
            ))

            # Prepare context with errors
            context = {
                "property_form": property_form,
                "image_forms": image_formset,
                "video_forms": video_formset,
                "image_form_errors": image_formset.errors,
                "video_form_errors": video_formset.errors,
            }
            return render(request, "properties/property_management.html", context)
    else:
        property_form = PropertyForm()
        image_formset = PropertyImageFormSet()
        video_formset = PropertyVideoFormSet()

    return render(
        request,
        "properties/property_management.html",
        {
            "property_form": property_form,
            "image_forms": image_formset,
            "video_forms": video_formset,
        },
    )


@login_required
@superuser_required
def toggle_sold_status(request, property_id):
    # Get the property object
    property = get_object_or_404(Property, id=property_id)
    
    # Toggle the "is_sold" status
    property.is_sold = not property.is_sold
    property.save()
    
    # Redirect back to the property list
    return redirect('all_properties')  # or the name of the property listing page
