from django.views.generic import ListView
from pockost_monitoring.ssl_monitor.models import SSLWebsite


class SSLWebsiteView(ListView):
    model = SSLWebsite
