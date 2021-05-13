from django.urls import path
from . import views
from django_filters.views import FilterView


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('others/', views.others, name="others"),
]
