from rest_framework import viewsets
from pockost_monitoring.api.serializers import ssl_website_serializers
from pockost_monitoring.ssl_monitor.models import SSLWebsite


class SSLWebsiteViewSet(viewsets.ModelViewSet):
    """
    Abitlity to view and edit website
    """

    queryset = SSLWebsite.objects.all()
    serializer_class = ssl_website_serializers.SSLWebsiteSerializer
