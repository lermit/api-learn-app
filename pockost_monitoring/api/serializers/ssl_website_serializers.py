from rest_framework import serializers
from pockost_monitoring.ssl_monitor.models import SSLWebsite


class SSLWebsiteSerializer(serializers.HyperlinkedModelSerializer):
    """The SSLWebsite Serializer.
    This class manage the JSON representation of a SSLWebsite object.
    """
    class Meta:
        model = SSLWebsite
        fields = '__all__'
