from django import forms


class CollectionForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=80, required=True)
    description = forms.CharField(label="Descripción", required=True)

class ConfirmDeleteForm(forms.Form):
    confirm = forms.BooleanField(label='Confirmar eliminación', required=True)
