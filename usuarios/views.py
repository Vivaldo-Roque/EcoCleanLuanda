from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from usuarios.forms import SignUpForm, SignInForm, UserDataForm

@login_required
def home(request):

    usuario = request.user

    context = {'usuario': usuario}

    return render(request, "inicio.html", context=context)

@login_required
def profile(request):
    if request.method == 'GET':

        usuario = request.user

        form = UserDataForm(initial={
                            'primeiro_nome': usuario.perfil.primeiro_nome,
                            'ultimo_nome': usuario.perfil.ultimo_nome,
                            'telefone': usuario.perfil.telefone,
                            'morada': usuario.perfil.morada,
                            }, request=request)

        context = {'usuario': usuario, 'form': form, 'feedback': ''}

        return render(request, "dadoscliente.html", context=context)

    elif request.method == 'POST':

        form = UserDataForm(request.POST, request=request)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Dados atualizados!")
                return HttpResponseRedirect('/perfil/')
            except:
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect('/perfil/')
        else:
            context = {'form': form, 'feedback': 'd-block'}
            return render(request, 'dadoscliente.html', context=context)

def signIn(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/inicio/')

    if request.method == 'GET':
        form = SignInForm(None)
        return render(request, 'entrar.html', context={'form': form, 'feedback': ''})
    elif request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            return form.singIn(request=request)
        else:
            return render(request, 'entrar.html', context={'form': form, 'feedback': 'd-block'})

def signUp(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/inicio/')

    if request.method == 'GET':
        form = SignUpForm(None)
        return render(request, 'registar.html', context={'form': form, 'feedback': ''})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request, "Sua conta foi criada, faça o login!")
                return HttpResponseRedirect('/entrar/')
            except:
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect('/registar/')
        else:
            return render(request, 'registar.html', context={'form': form, 'feedback': 'd-block'})

def about(request):
    return render(request, "sobre.html")

@login_required
def delete_account(request):
    if request.method == 'POST':
        if 'eliminar_conta' in request.POST:
            usuario = request.user
            logout(request)
            usuario.delete()
            messages.success(request, "Conta deletada!")
            return HttpResponseRedirect('/entrar/')

@login_required
def my_logout(request):
    logout(request)
    messages.success(request, "Deslogado!")
    return HttpResponseRedirect('/')
