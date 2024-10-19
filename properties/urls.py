from django.urls import path

from .views import (AllProperties, PropertyDetail, like_property,
                    property_management, toggle_sold_status)

urlpatterns = [
    path("properties/", AllProperties.as_view(), name="all_properties"),
    path(
        "properties/<int:property_id>/",
        PropertyDetail.as_view(),
        name="property_detail",
    ),
    path("like-property/<int:property_id>/", like_property, name="like_property"),
    path("manage/", property_management, name="property_management"),
    path('property/<int:property_id>/toggle-sold/', toggle_sold_status, name='toggle_sold_status'),
]
