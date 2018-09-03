from django.conf.urls import url, include
from rest_framework import routers
from pockost_monitoring.api import views


router = routers.DefaultRouter()
router.register(r'ssl_monitor', views.SSLWebsiteViewSet)

urlpatterns = [
    url(
        r'^',
        include(router.urls)
    ),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    )
]
