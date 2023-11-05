from django import forms
from django.forms import ModelForm, TextInput
from contentoreslixo.models import ContentorLixo

class ContainerForm(ModelForm):
    class Meta:
        model = ContentorLixo
        fields = ['nome', 'descricao', 'localizacao', 'geolocalizacao']

    nome = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': '',
        'id': 'floatingName',
        'type': 'text'
    }))
    descricao = forms.CharField(required=False, max_length=255, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': '',
        'id': 'floatingDescription',
        'type': 'text'
    }))
    localizacao = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': '',
        'id': 'floatingLocation',
        'type': 'text'
    }))
    geolocalizacao = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': '',
        'id': 'floatingGeoLocation',
        'type': 'text'
    }))

    def clean(self):
        super(ContainerForm, self).clean()

        # getting fields from cleaned_data
        nome = self.cleaned_data.get('nome')
        descricao = self.cleaned_data.get('descricao')
        localizacao = self.cleaned_data.get('localizacao')
        geolocalizacao = self.cleaned_data.get('geolocalizacao')

        # validating the email and password

        if nome == "" or nome.isspace():
            self._errors['nome'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if descricao == "" or descricao.isspace():
            self._errors['descricao'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if localizacao == "" or localizacao.isspace():
            self._errors['localizacao'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if geolocalizacao == "" or geolocalizacao.isspace():
            self._errors['geolocalizacao'] = self.error_class(
                ['Campo não pode estar vazio!'])

        return self.cleaned_data
