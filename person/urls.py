from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path('api/<int:id>', views.PersonCustomView.as_view()),
    path('api', views.create_person, name='create_person'),
]
