from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PersonCustomView

router = DefaultRouter()

urlpatterns = [
    path('api', PersonCustomView.as_view() )
]
