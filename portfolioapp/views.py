from django.shortcuts import render, redirect
from . models import Aboutme, Count, Skill, Interest

from .forms import ContactForm


# Create your views here.
def home(request):
    aboutme = Aboutme.objects.get(name='Zahid Hasan Milu')
    count = Count.objects.all()
    technical_skil = Skill.objects.all()
    interest = Interest.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    context ={
        'aboutme': aboutme,
        'count':count,
        'technical_skil':technical_skil,
        'interest':interest,
        'form':form
    }
    return render(request, 'portfolio/index.html', context)

