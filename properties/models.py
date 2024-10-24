from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Property(models.Model):
    PROPERTY_TYPES = [
        ("Bilocali", "Bilocali"),
        ("Trilocali", "Trilocali"),
        # Add other types as needed
    ]

    LOCATIONS = [
        ("Oristano", "Oristano"),
        # Add other locations as needed
    ]

    name = models.CharField(max_length=255, default="")
    features = models.TextField(default="")
    main_image = CloudinaryField("image", blank=True, null=True)  # Main image for cards
    main_video = models.FileField(
        upload_to="videos/",
        blank=True,
        null=True,
        storage=VideoMediaCloudinaryStorage(),
        validators=[validate_video],
    )  # Main video for cards
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    size = models.PositiveIntegerField()
    is_sold = models.BooleanField(default=False, verbose_name="Sold Status")

    location = models.CharField(max_length=100, choices=LOCATIONS, default="Oristano")
    property_type = models.CharField(
        max_length=50, choices=PROPERTY_TYPES, default="Trilocali"
    )

    # Adding a ManyToManyField to track which users have liked this property
    liked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="liked_properties", blank=True
    )

    def __str__(self):
        return self.name

    def number_of_likes(self):
        """Returns the number of users who liked this property."""
        return self.liked_by.count()
    
    def get_absolute_url(self):
        """Returns the URL for the property detail page."""
        return reverse('property_detail', kwargs={'property_id': self.id})

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ["-created_at"]  # Default ordering: most recent first


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, related_name="images", on_delete=models.CASCADE
    )
    image = CloudinaryField("image")

    def __str__(self):
        return f"Image for {self.property.name}"


class PropertyVideo(models.Model):
    property = models.ForeignKey(
        Property, related_name="videos", on_delete=models.CASCADE
    )
    video = models.FileField(
        upload_to="videos/",
        blank=True,
        storage=VideoMediaCloudinaryStorage(),
        validators=[validate_video],
    )

    def __str__(self):
        return f"Video for {self.property.name}"
