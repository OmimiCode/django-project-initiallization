from django.urls import path

from pentax.views import home

urlpatterns = [
    path('', home, name='homeurl')
]