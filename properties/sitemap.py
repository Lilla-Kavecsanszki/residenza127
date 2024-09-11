from django.contrib.sitemaps import Sitemap
from .models import Property

class PropertySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Property.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return f"/properties/{obj.id}/"  # Customize this based on your URL pattern



sitemaps = {
    'properties': PropertySitemap,
}