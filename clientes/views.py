from django.shortcuts import render
from .models import Person

# Create your views here.
def persons_list(request):
    persons = Person.object.all()
    return render(request, 'pessoa.html')


