from django import forms
from filme.models import Filme


class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'sinopse', 'anoLancamento', 'diretor', 'genero']
