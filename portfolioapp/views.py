from django.shortcuts import render, redirect
from . models import Aboutme, Count, Skill, Interest, Summary, Degree, Department, Education,Professional_Experience
from .forms import ContactForm


# Create your views here.
def home(request):
    aboutme = Aboutme.objects.get(name='Zahid Hasan Milu')
    count = Count.objects.all()
    technical_skil = Skill.objects.all()
    interest = Interest.objects.all()
    summary = Summary.objects.all()
    education = Education.objects.all()
    pExperience = Professional_Experience.objects.all()

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
        'form':form,
        'summary':summary,
        'education':education,
        'pExperience': pExperience,

    }
    return render(request, 'portfolio/index.html', context)

