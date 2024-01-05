from django import forms
from django.forms import ModelForm, TextInput, EmailInput, input
from django.http import HttpResponseRedirect
from PlatformReciclagem.models import Comprador, Vendedor, Venda
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Group

PROVINCIA_CHOICES = [
        ('', 'Escolha uma Província...'),
        ('Bengo', 'Bengo'),
        ('Benguela', 'Benguela'),
        ('Bié', 'Bié'),
        ('Cabinda', 'Cabinda'),
        ('Cuando Cubango', 'Cuando Cubango'),
        ('Cuanza Norte', 'Cuanza Norte'),
        ('Cuanza Sul', 'Cuanza Sul'),
        ('Cunene', 'Cunene'),
        ('Huambo', 'Huambo'),
        ('Huíla', 'Huíla'),
        ('Luanda', 'Luanda'),
        ('Lunda Norte', 'Lunda Norte'),
        ('Lunda Sul', 'Lunda Sul'),
        ('Malanje', 'Malanje'),
        ('Moxico', 'Moxico'),
        ('Namibe', 'Namibe'),
        ('Uíge', 'Uíge'),
        ('Zaire', 'Zaire'),
    ]

TIPO_MATERIAL_RECICLAVEL_CHOICES = [
        ('', 'Escolha um material...'),
        ('Metal', 'Metal'),
        ('Plástico', 'Plástico')
    ]

class SellerForm(forms.Form):
    class Meta:
        model = Vendedor
        fields = ['nome_completo', 'email', 'telefone', 'provincia', 'endereco', 'tipo_material_reciclavel', 'quantidade', 'descricao', 'peso_total']

    nome_completo = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'seu nome completo',
        'id': 'fullname'
    }))

    email = forms.EmailField(required=False, max_length=100, widget=EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu E-mail',
        'id': 'email',
    }))

    numero_telefone = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu contacto',
        'id': 'phonenumber',
        'type': 'number'
    }))

    provincia = forms.ChoiceField(choices=PROVINCIA_CHOICES, required=False, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'province'
        }))

    endereco = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu contacto',
        'id': 'phonenumber',
        'type': 'number'
    }))

    tipo_material_reciclavel = forms.ChoiceField(choices=TIPO_MATERIAL_RECICLAVEL_CHOICES, required=False, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'recyclable_material'
        }))

    quantidade = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite a quantidade',
        'id': 'quantity',
        'type': 'number'
    }))

    descricao = forms.Textarea(required=False, max_length=1024, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'product_description',
        'cols': '40',
        'rows': '5'
        }))

    peso_total = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite o peso total',
        'id': 'weight',
        'type': 'number'
    }))

    def clean(self):
        super(SellerForm, self).clean()

        # getting email and password from cleaned_data
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # validating the email and password

        if email == "" or email.isspace():
            self._errors['email'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if password == "" or password.isspace():
            self._errors['password'] = self.error_class(
                ['Campo não pode estar vazio!'])

        return self.cleaned_data

    def singIn(self, request):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            usuario_aux = User.objects.get(email=email)
            password = self.cleaned_data['password']
            usuario = authenticate(request, username=usuario_aux.username, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, "Logado!")
                return HttpResponseRedirect('/inicio/')
            else:
                messages.error(request, "E-mail ou senha inválidos!")
                return HttpResponseRedirect('/entrar/')
        else:
            messages.error(request, "E-mail ou senha inválidos!")
            return HttpResponseRedirect('/entrar/')
        
class BuyerForm(forms.Form):
    class Meta:
        model = Comprador
        fields = ['nome_completo', 'email', 'telefone', 'provincia', 'endereco', 'tipo_material_reciclavel', 'quantidade', 'descricao']

    nome_completo = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'seu nome completo',
        'id': 'fullname'
    }))

    email = forms.EmailField(required=False, max_length=100, widget=EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu E-mail',
        'id': 'email',
    }))

    numero_telefone = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu contacto',
        'id': 'phonenumber',
        'type': 'number'
    }))

    provincia = forms.ChoiceField(choices=PROVINCIA_CHOICES, required=False, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'province'
        }))

    endereco = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu contacto',
        'id': 'phonenumber',
        'type': 'number'
    }))

    tipo_material_reciclavel = forms.ChoiceField(choices=TIPO_MATERIAL_RECICLAVEL_CHOICES, required=False, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'recyclable_material'
        }))

    quantidade = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite a quantidade',
        'id': 'quantity',
        'type': 'number'
    }))

    descricao = forms.Textarea(required=False, max_length=1024, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'product_description',
        'cols': '40',
        'rows': '5'
        }))

    def clean(self):
        super(BuyerForm, self).clean()

        # getting email and password from cleaned_data
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        # validating the email and password

        if email == "" or email.isspace():
            self._errors['email'] = self.error_class(
                ['Campo não pode estar vazio!'])

        if password == "" or password.isspace():
            self._errors['password'] = self.error_class(
                ['Campo não pode estar vazio!'])

        return self.cleaned_data

    def singIn(self, request):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            usuario_aux = User.objects.get(email=email)
            password = self.cleaned_data['password']
            usuario = authenticate(request, username=usuario_aux.username, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, "Logado!")
                return HttpResponseRedirect('/inicio/')
            else:
                messages.error(request, "E-mail ou senha inválidos!")
                return HttpResponseRedirect('/entrar/')
        else:
            messages.error(request, "E-mail ou senha inválidos!")
            return HttpResponseRedirect('/entrar/')