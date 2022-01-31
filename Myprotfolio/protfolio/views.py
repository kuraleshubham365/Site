from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import ContactForm
from .models import Contact

# Create your views here.
#@csrf_protect
def index(request):
    context={}
    """ this is for class baesd input form """
    form = ContactForm()
    context = {'form':form}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    """ this is for custome html input form
    if request.method == 'POST':
        contact = Contact()
        name = request.method.POST.get('Name')
        tele = request.method.POST.get('mobile')
        email = request.method.POST.get('email')
        cmp_n = request.method.POST.get('c_name')
        sub = request.method.POST.get('subject')
        msg = request.method.POST.get('msg')
        contact.save()
        return redirect('index')
    """
    return render(request, 'protfolio/index.html', context)

def skills(request):
    return render(request, 'protfolio/skills.html')

def about(request):
    return render(request, 'protfolio/about.html')
