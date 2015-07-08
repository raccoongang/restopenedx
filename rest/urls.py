from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest import views

urlpatterns = [
    url(r'^tracking_log/$', views.TrackingLogView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)