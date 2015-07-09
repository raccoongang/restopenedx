from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest import views

urlpatterns = [
    url(r'^api/score/$', views.ScoreView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
