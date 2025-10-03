from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'priority', 'due_date', 'assigned_to']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Inserisci il titolo del task'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descrizione dettagliata (facoltativa)'
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'es: Lavoro, Personale, Studio'
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'assigned_to': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'title': 'Titolo *',
            'description': 'Descrizione',
            'category': 'Categoria',
            'priority': 'Priorità',
            'due_date': 'Data di scadenza',
            'assigned_to': 'Assegna a utente',
        }