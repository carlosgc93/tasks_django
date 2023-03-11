from asyncio import Task
from dataclasses import field
from tkinter import Widget
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields = ['title','description','important']
        widgets = {'title': forms.TextInput (attrs={'class':'form-control', 'placeholder': 'Escribe titulo de tarea'}), 'descrption': forms.Textarea (attrs={'class':'form-control', 'placeholder': 'Escribe la descrpcion'}),'important': forms.CheckboxInput (attrs={'class':'form-check-input'})}