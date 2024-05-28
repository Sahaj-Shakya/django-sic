from django.shortcuts import render

# Create your views here.
def courses(request):
    return render (request, 'lms/courses.html')

def bca_view(request):
    return render(request, 'lms/bca.html')

def ca_view(request):
    return render(request, 'lms/ca.html')

def bbm_view(request):
    return render(request, 'lms/bbm.html')

def bbs_view(request):
    return render(request, 'lms/bbs.html')