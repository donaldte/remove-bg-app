from django.urls import path

from . import views

app_name = 'images_app'


urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
]