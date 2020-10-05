from django import forms

from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        exclude = ('estado',)

        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Por favor. Ingrese su nombre.',
                }
            ),
            'correo':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Por favor. Ingrese su correo electronico.',
                }
            ),
            'asunto':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Por favor. Ingrese el tema.',
                }
            ),
            'mensaje':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Escriba su mensaje.',
                }
            ),
        }