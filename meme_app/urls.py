from .views import *
from django.urls import path

app_name = 'meme_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('about-us', about_us, name='about-us'),
    path('ca', ca_view, name='ca'),
    path('bbs', bbs_view, name='bbs'),
    path('bbm', bbm_view, name='bbm'),
    path('bca', bca_view, name='bca'),
]