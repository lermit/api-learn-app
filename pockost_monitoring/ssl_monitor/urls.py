from django.urls import path
from pockost_monitoring.ssl_monitor import views

urlpatterns = [
    path('websites/', views.SSLWebsiteView.as_view()),
    ]
