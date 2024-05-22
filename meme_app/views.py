from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about.html')

def bca_view(request):
    return render(request, 'bca.html')

def ca_view(request):
    return render(request, 'ca.html')

def bbm_view(request):
    return render(request, 'bbm.html')

def bbs_view(request):
    return render(request, 'bbs.html')

