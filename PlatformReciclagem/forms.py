from django import forms
from django.forms import TextInput, EmailInput, ChoiceField
from PlatformReciclagem.models import Comprador, Vendedor, Venda
from django.forms import ModelForm

PROVINCIA_CHOICES = [
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
        ('Metal', 'Metal'),
        ('Plástico', 'Plástico')
    ]

class SellerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        disabled = kwargs.pop("disabled", None)
        super(SellerForm, self).__init__(*args, **kwargs)

        if disabled:
            for key, field in self.fields.items():
                field.disabled = disabled


    class Meta:
        model = Vendedor
        fields = ['nome_completo', 'email', 'telefone', 'provincia', 'endereco', 'tipo_material_reciclavel', 'quantidade', 'descricao', 'peso_total']

    nome_completo = forms.CharField(required=True, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'seu nome completo',
        'id': 'fullname'
    }))

    email = forms.EmailField(required=True, max_length=100, widget=EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu E-mail',
        'id': 'email'
    }))

    telefone = forms.CharField(required=True, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu contacto',
        'id': 'phonenumber',
        'type': 'number'
    }))

    provincia = forms.ChoiceField(choices=PROVINCIA_CHOICES, required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'province'
        }))

    endereco = forms.CharField(required=True, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu endereço',
        'id': 'address'
    }))

    tipo_material_reciclavel = forms.ChoiceField(choices=TIPO_MATERIAL_RECICLAVEL_CHOICES, required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'recyclable_material'
        }))

    quantidade = forms.CharField(required=True, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite a quantidade',
        'id': 'quantity',
        'type': 'number'
    }))

    descricao = forms.CharField(widget=forms.Textarea(attrs={
        'required': True,
        'max_length': 1024,
        'class': 'form-control',
        'id': 'product_description',
        'cols': '40',
        'rows': '5'
        }))

    peso_total = forms.CharField(required=True, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite o peso total',
        'id': 'weight',
        'type': 'number'
    }))
        
class BuyerForm(ModelForm):

    def __init__(self, *args, **kwargs):
        disabled = kwargs.pop("disabled", None)
        super(BuyerForm, self).__init__(*args, **kwargs)
        
        if disabled:
            for key, field in self.fields.items():
                field.disabled = disabled

    class Meta:
        model = Comprador
        fields = ['nome_completo', 'email', 'telefone', 'provincia', 'endereco', 'tipo_material_reciclavel', 'quantidade_desejada', 'descricao']

    nome_completo = forms.CharField(required=True, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'seu nome completo',
        'id': 'fullname'
    }))

    email = forms.EmailField(required=True, max_length=100, widget=EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu E-mail',
        'id': 'email'
    }))

    telefone = forms.CharField(required=True, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu contacto',
        'id': 'phonenumber',
        'type': 'number'
    }))

    provincia = forms.ChoiceField(choices=PROVINCIA_CHOICES, required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'province'
        }))

    endereco = forms.CharField(required=True, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite seu endereço',
        'id': 'address'
    }))

    tipo_material_reciclavel = forms.ChoiceField(choices=TIPO_MATERIAL_RECICLAVEL_CHOICES, required=True, widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'recyclable_material'
        }))

    quantidade_desejada = forms.CharField(required=True, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite a quantidade',
        'id': 'quantity',
        'type': 'number'
    }))

    descricao = forms.CharField(widget=forms.Textarea(attrs={
        'required': True,
        'max_length': 1024,
        'class': 'form-control',
        'id': 'product_description',
        'cols': '40',
        'rows': '5'
        }))                

class SalesForm(ModelForm):

    def __init__(self, *args, **kwargs):
        disabled = kwargs.pop("disabled", None)
        super(SalesForm, self).__init__(*args, **kwargs)
        
        if disabled:
            for key, field in self.fields.items():
                field.disabled = disabled

    class Meta:
        model = Venda
        fields = ['comprador', 'vendedor', 'valor']

    comprador = forms.ModelChoiceField(queryset=Comprador.objects.all(), widget=forms.Select(attrs={
        'class': "form-control",
        'placeholder': 'Digite o id do comprador',
        'id': 'buyer',
        'type': 'number'
    }))

    vendedor = forms.ModelChoiceField(queryset=Vendedor.objects.all(), widget=forms.Select(attrs={
        'class': "form-control",
        'placeholder': 'Digite o id do vendedor',
        'id': 'seller',
        'type': 'number'
    }))

    valor = forms.CharField(required=False, max_length=100, widget=TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Digite o valor',
        'id': 'valor',
        'type': 'number'
    }))