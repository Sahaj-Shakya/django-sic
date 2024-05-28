from django.urls import path
from .views import *

app_name = 'lms'

urlpatterns = [
    path('courses/', courses, name='courses'),
    path('ca/', ca_view, name='ca'),
    path('bbs/', bbs_view, name='bbs'),
    path('bbm/', bbm_view, name='bbm'),
    path('bca/', bca_view, name='bca'),
]