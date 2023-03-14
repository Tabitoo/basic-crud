from django import forms

class CreateNewNote(forms.Form):
    title = forms.CharField(label="Titulo de la nota", max_length=200)
    description = forms.CharField(label="Descripcion de la nota", widget=forms.Textarea)
