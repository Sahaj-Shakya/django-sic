from django.shortcuts import render
from .forms import ContactForm
from.models import Contact

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, './meme_app/about.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form.data)
    
    form = ContactForm()
    
    context = {
        'form': form
    }
    return render(request, 'meme_app/contact.html', context)

