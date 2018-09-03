from django.db import models


# SSLWebsite
class SSLWebsite(models.Model):
    """SSLWebsite model contain all website that should be
    monitored
    """

    # Website URL
    # TODO : Have a validator for domain+port
    # URLField alway append a http:// prefix
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.url
