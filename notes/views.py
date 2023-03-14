from django.shortcuts import render, redirect
from .forms import CreateNewNote
from .models import Note

# Create your views here.

def index(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        return render(request, "index.html", { "form" : CreateNewNote(), "notes" : notes })
    else:
        Note.objects.create(title=request.POST['title'], description=request.POST['description'])
        return redirect("index")

