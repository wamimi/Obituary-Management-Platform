from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Obituary
from django.utils.text import slugify

def generate_unique_slug(name):
    slug = slugify(name)
    unique_slug = slug
    num = 1
    while Obituary.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{num}"
        num += 1
    return unique_slug

def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST['author']
        
        slug = generate_unique_slug(name)
        
        obituary = Obituary(
            name=name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            content=content,
            author=author,
            slug=slug
        )
        obituary.save()

        return HttpResponse('Obituary submitted successfully.')
    else:
        return render(request, 'obituaries/obituary_form.html')

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'obituaries/view_obituaries.html', {'obituaries': obituaries})
