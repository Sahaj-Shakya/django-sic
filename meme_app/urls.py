from .views import *
from django.urls import path

app_name = 'meme_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('about-us/', about_us, name='about-us'),
    path('contact-us/', contact_us, name='contact-us'),
    
    
]