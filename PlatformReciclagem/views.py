from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from usuarios.decorators import allowed_users
from PlatformReciclagem.forms import SellerForm, BuyerForm, SalesForm
from django.contrib import messages
from PlatformReciclagem.models import Venda, Vendedor, Comprador

@login_required
@allowed_users(allowed_roles=['admin'])
def dashboard(request):

    usuario = request.user

    context = {'usuario': usuario}

    return render(request, "dashboard.html", context=context)

@login_required
@allowed_users(allowed_roles=['admin'])
def sales(request):

    usuario = request.user

    venda = Venda.objects.all() 

    context = {'usuario': usuario, 'vendas': venda}

    return render(request, "vendas.html", context=context)
 
def seller_view(request):

    usuario = request.user

    if request.method == 'GET':

        form = SellerForm()

        context = {'usuario': usuario, 'form': form, 'feedback': ''}

        return render(request, "vender.html", context=context)

    elif request.method == 'POST':

        form = SellerForm(request.POST)

        if form.is_valid():
            try:
                instance = form.save()
                messages.success(request, f"Dados enviados. Guarde este número (#{instance.id}) do seu formulário. Entraremos em contacto, por favor aguarde!")
                return HttpResponseRedirect('/inicio/')
            except:
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect('/vender/')
        else:
            context = {'form': form, 'feedback': 'd-block'}
            return render(request, 'vender.html', context=context)
        
def buyer_view(request):

    usuario = request.user

    if request.method == 'GET':

        form = BuyerForm()

        context = {'usuario': usuario, 'form': form, 'feedback': ''}

        return render(request, "comprar.html", context=context)

    elif request.method == 'POST':

        form = BuyerForm(request.POST)

        if form.is_valid():
            try:
                instance = form.save()
                messages.success(request, f"Dados enviados. Guarde este número (#{instance.id}) do seu formulário. Entraremos em contacto, por favor aguarde!")
                return HttpResponseRedirect('/inicio/')
            except:
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect('/comprar/')
        else:
            context = {'form': form, 'feedback': 'd-block'}
            return render(request, 'comprar.html', context=context)

@login_required
@allowed_users(allowed_roles=['admin'])
def buyers_view(request):
    usuario = request.user

    compradores = Comprador.objects.all() 

    context = {'usuario': usuario, 'compradores': compradores}

    return render(request, "compradores.html", context=context)

@login_required
@allowed_users(allowed_roles=['admin'])
def sellers_view(request):
    usuario = request.user

    vendedores = Vendedor.objects.all() 

    context = {'usuario': usuario, 'vendedores': vendedores}

    return render(request, "vendedores.html", context=context)

def environmental_education_view(request):

    return render(request, 'educacaoambiental.html')

@login_required
@allowed_users(allowed_roles=['admin'])
def add_sale(request):

    usuario = request.user

    if request.method == 'GET':

        form = SalesForm()

        context = {'usuario': usuario, 'form': form, 'feedback': ''}

        return render(request, "adicionarvenda.html", context=context)

    elif request.method == 'POST':

        form = SalesForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Venda adicionada com sucesso!")
                return HttpResponseRedirect('/inicio/')
            except:
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect('/vender/')
        else:
            context = {'form': form, 'feedback': 'd-block'}
            return render(request, 'adicionarvenda.html', context=context)

@login_required
@allowed_users(allowed_roles=['admin'])
def see_sale(request, id):  
    
    venda = Venda.objects.get(id=id)

    form1 = SellerForm(disabled=True, instance=venda.vendedor)
    form2 = BuyerForm(disabled=True, instance=venda.comprador)
    form3 = SalesForm(disabled=True, instance=venda)

    return render(request,'vervenda.html', {'form1':form1, 'form2':form2, 'form3':form3})  

@login_required
@allowed_users(allowed_roles=['admin'])
def update_sale(request, id):  

    venda = Venda.objects.get(id=id)  

    if request.method == 'GET':

        form = SalesForm(instance=venda)

        context = {'form': form, 'feedback': ''}

        return render(request, "atualizarvenda.html", context=context)

    elif request.method == 'POST':

        form = SalesForm(request.POST, instance=venda)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Dados atualizados!")
                return HttpResponseRedirect('/vendas/')
            except:
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect(request.path_info)
        else:
            context = {'form': form, 'feedback': 'd-block'}
            return render(request, 'atualizarvenda.html', context=context)

@login_required
@allowed_users(allowed_roles=['admin'])
def destroy_sale(request, id):  
    venda = Venda.objects.get(id=id)  
    venda.delete()  
    return redirect("/vendas/") 

@login_required
@allowed_users(allowed_roles=['admin'])
def see_seller(request, id):  
    vendedor = Vendedor.objects.get(id=id) 
    form = SellerForm(instance=vendedor, disabled=True)
    return render(request,'vervendedor.html', {'form':form})

@login_required
@allowed_users(allowed_roles=['admin'])
def update_seller(request, id):  

    vendedor = Vendedor.objects.get(id=id)  

    if request.method == 'GET':

        form = SellerForm(instance=vendedor)

        context = {'form': form, 'feedback': ''}

        return render(request, "editarvendedor.html", context=context)

    elif request.method == 'POST':

        form = SellerForm(request.POST, instance=vendedor)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Dados atualizados!")
                return HttpResponseRedirect('/vendedores/')
            except:
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect(request.path_info)
        else:
            context = {'form': form, 'feedback': 'd-block'}
            return render(request, 'editarvendedor.html', context=context)

@login_required
@allowed_users(allowed_roles=['admin'])
def destroy_seller(request, id):  
    venda = Vendedor.objects.get(id=id)  
    venda.delete()  
    return redirect("/vendedores/") 

@login_required
@allowed_users(allowed_roles=['admin'])
def see_buyer(request, id):  
    comprador = Comprador.objects.get(id=id) 
    form = BuyerForm(instance=comprador, disabled=True)
    return render(request,'vercomprador.html', {'form':form}) 

@login_required
@allowed_users(allowed_roles=['admin'])
def update_buyer(request, id):  

    if request.method == 'GET':

        comprador = Comprador.objects.get(id=id)  
        form = BuyerForm(instance=comprador)

        context = {'form': form, 'feedback': ''}

        return render(request, "editarcomprador.html", context=context)

    elif request.method == 'POST':

        comprador = Comprador.objects.get(id=id)
        form = BuyerForm(request.POST, instance=comprador)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, f"Dados atualizados!")
                return HttpResponseRedirect('/compradores/')
            except:
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect(request.path_info)
        else:
            context = {'form': form, 'feedback': 'd-block'}
            return render(request, 'editarcomprador.html', context=context) 

@login_required
@allowed_users(allowed_roles=['admin'])
def destroy_buyer(request, id):  
    venda = Comprador.objects.get(id=id)  
    venda.delete()  
    return redirect("/compradores/") 
