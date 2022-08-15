from django.urls import path
from .views import home, createShortURL, redirectURL


urlpatterns = [
    path('', home, name='home'),
    path('create/', createShortURL, name='create'),
    path('<str:url>', redirectURL, name='redirect')
]
