import json
import os
from usuarios.decorators import allowed_users
from contentoreslixo.models import ContentorLixo
from rest_framework import viewsets
from rest_framework import permissions
from contentoreslixo.serializers import ContetorLixoSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from sensores.models import DadoSensor
from datetime import datetime, timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from contentoreslixo.forms import ContainerForm

class ContentorLixoViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ContentorLixo.objects.all()
    serializer_class = ContetorLixoSerializer
    permission_classes = [permissions.IsAuthenticated]

@login_required
@allowed_users(allowed_roles=['admin'])
def dashboard(request):

    usuario = request.user

    context = {'usuario': usuario}

    return render(request, "dashboard.html", context=context)

# @login_required
def containers(request):

    usuario = request.user
    data = []
    containers = ContentorLixo.objects.all()
    for c in containers:

        try:
            containerSensor = DadoSensor.objects.filter(contentor=c.id).latest("created_at")
            currentDateOnSystem = datetime.now(timezone.utc)
            diff = currentDateOnSystem - containerSensor.created_at
            minutes = diff.seconds / 60
            if minutes > 5:
                status = False
            else:
                status = True
            data.append({
            "contentor": str(containerSensor.contentor.id),
            "nome": c.nome,
            "descricao": c.descricao,
            "localizacao": c.localizacao,
            "geolocalizacao": c.geolocalizacao,
            "sensor_distancia": containerSensor.sensor_distancia,
            "sensor_umidade": containerSensor.sensor_umidade,
            "sensor_temperatura": containerSensor.sensor_temperatura,
            "sensor_chuva": containerSensor.sensor_chuva,
            "status": status
            })
        except DadoSensor.DoesNotExist:
            data.append({
            "contentor": str(c.id),
            "nome": c.nome,
            "descricao": c.descricao,
            "localizacao": c.localizacao,
            "geolocalizacao": c.geolocalizacao
            })

    context = {'contentores': data, 'usuario': usuario}

    return render(request, "contentores.html", context=context)

@login_required
@allowed_users(allowed_roles=['admin'])
def add_container(request):

    usuario = request.user

    if request.method == "GET":
        form = ContainerForm(None)
        context = {'form': form, 'usuario': usuario, 'feedback': ''}
        return render(request, "adicionarcontentor.html", context=context)
    
    if request.method == "POST":

        form = ContainerForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Container adicionado!")
                return HttpResponseRedirect('/contentores/')
            except Exception as e:
                print(e)
                messages.error(request, "Por favor tente novamente!")
                return HttpResponseRedirect('/contentores/')
        else:
            context = {'form': form, 'usuario': usuario, 'feedback': 'd-block'}
            return render(request, 'adicionarcontentor.html', context=context)

@login_required
@allowed_users(allowed_roles=['admin'])
def edit_container(request):

    usuario = request.user
 
    if request.method == "POST":

        if 'btn_edit' in request.POST:
            id = request.POST.get('cid')
            contentor = ContentorLixo.objects.get(id=id)
            form = ContainerForm(
                initial={
                                'nome': contentor.nome,
                                'descricao': contentor.descricao,
                                'localizacao': contentor.localizacao,
                                'geolocalizacao': contentor.geolocalizacao,
                                }
            )
            context = {'form': form, 'usuario': usuario}
            response = render(request, "editarcontentor.html", context=context)
            response.set_cookie('cid', id)
            return response
        
        elif 'btn_save' in request.POST:
        
            id = request.COOKIES.get('cid')
            contentor = ContentorLixo.objects.get(id=id)
            form = ContainerForm(request.POST, instance=contentor)

            if form.is_valid():
                print("valid form!")
                try:
                    form.save()
                    messages.success(request, "Container editado!")
                    return HttpResponseRedirect('/contentores/')
                except:
                    messages.error(request, "Por favor tente novamente!")
                    return HttpResponseRedirect('/editarcontentor/')
            else:
                context = {'form': form, 'usuario': usuario, 'feedback': 'd-block'}
                return render(request, 'editarcontentor.html', context=context)

    elif request.method == "GET":
        id = request.COOKIES.get('cid')
        contentor = ContentorLixo.objects.filter(id=id).first()
        form = ContainerForm(
            initial={
                            'nome': contentor.nome,
                            'descricao': contentor.descricao,
                            'localizacao': contentor.localizacao,
                            'geolocalizacao': contentor.geolocalizacao,
                            }
        )
        context = {'form': form, 'usuario': usuario}
        response = render(request, "editarcontentor.html", context=context)
        response.set_cookie('cid', id)
        return response

# @login_required
def containerdetails(request):

    map_api_key = os.getenv('GOOGLE_MAP_API_KEY')
    usuario = request.user
        
    data = {}
    if request.method == "POST":
        id = request.POST.get("id")
    elif request.method == "GET":
        id = request.COOKIES.get('cid')
    
    try:
        if DadoSensor.objects.filter(contentor=id).exists():
            containerSensor = DadoSensor.objects.filter(contentor=id).latest("created_at")
            currentDateOnSystem = datetime.now(timezone.utc)
            diff = currentDateOnSystem - containerSensor.created_at
            minutes = diff.seconds / 60
            if minutes > 5:
                status = False
            else:
                status = True
            data = {
            "contentor": str(containerSensor.contentor.id),
            "nome": containerSensor.contentor.nome,
            "descricao": containerSensor.contentor.descricao,
            "localizacao": containerSensor.contentor.localizacao,
            "geolocalizacao": containerSensor.contentor.geolocalizacao,
            "sensor_distancia": containerSensor.sensor_distancia,
            "sensor_umidade": containerSensor.sensor_umidade,
            "sensor_temperatura": containerSensor.sensor_temperatura,
            "sensor_chuva": containerSensor.sensor_chuva,
            "status": status
            }
        else:
            contentor = ContentorLixo.objects.filter(id=id).first()
            data = {
            "contentor": str(contentor.id),
            "nome": contentor.nome,
            "descricao": contentor.descricao,
            "localizacao": contentor.localizacao,
            "geolocalizacao": contentor.geolocalizacao,
            "sensor_distancia": 0,
            "sensor_umidade": 0,
            "sensor_temperatura": 0,
            "sensor_chuva": 0,
            "status": False
            }

    except DadoSensor.DoesNotExist:
        contentor = ContentorLixo.objects.filter(id=id).first()
        data = {
        "contentor": str(contentor.id),
        "nome": contentor.nome,
        "descricao": contentor.descricao,
        "localizacao": contentor.localizacao,
        "geolocalizacao": contentor.geolocalizacao,
        "sensor_distancia": 0,
        "sensor_umidade": 0,
        "sensor_temperatura": 0,
        "sensor_chuva": 0,
        "status": False
        }
        
    context = {'contentor': data, 'map_api_key': map_api_key, 'usuario': usuario}
    response = render(request, "contentordetalhes.html", context=context)
    response.set_cookie('cid', id)
    return response

# @login_required
def check_if_device_is_online(request):
    if request.method == 'GET':
        data = []
        containers = ContentorLixo.objects.all()
        for c in containers:
            containerSensor = DadoSensor.objects.filter(contentor=c.id).latest("created_at")
            currentDateOnSystem = datetime.now(timezone.utc)
            diff = currentDateOnSystem - containerSensor.created_at
            minutes = diff.seconds / 60
            if minutes > 5:
                status = "off"
            else:
                status = "on"
            data.append({
            "contentor": str(containerSensor.contentor.id),
            "nome": c.nome,
            "descricao": c.descricao,
            "localizacao": c.localizacao,
            "geolocalizacao": c.geolocalizacao,
            "sensor_distancia": containerSensor.sensor_distancia,
            "sensor_umidade": containerSensor.sensor_umidade,
            "sensor_temperatura": containerSensor.sensor_temperatura,
            "sensor_chuva": containerSensor.sensor_chuva,
            "status": status
            })
        return HttpResponse(json.dumps(data, indent=2))
        
@login_required
@allowed_users(allowed_roles=['admin'])
def delete_container(request):
    if request.method == 'POST':
        if 'deletar_contentor' in request.POST:
            cid = request.POST['cid']
            contentor = ContentorLixo.objects.filter(id=cid).first()
            contentor.delete()
            messages.success(request, "Contentor deletado!")
            return HttpResponseRedirect('/contentores/')

# @login_required
def chart_data(request, id):
    try:
        if DadoSensor.objects.filter(contentor=id).exists():
            containerSensor = DadoSensor.objects.filter(contentor=id).latest("created_at")
            currentDateOnSystem = datetime.now(timezone.utc)
            diff = currentDateOnSystem - containerSensor.created_at
            minutes = diff.seconds / 60
            if minutes > 5:
                status = False
            else:
                status = True
            data = {
            "contentor": str(containerSensor.contentor.id),
            "nome": containerSensor.contentor.nome,
            "descricao": containerSensor.contentor.descricao,
            "localizacao": containerSensor.contentor.localizacao,
            "geolocalizacao": containerSensor.contentor.geolocalizacao,
            "sensor_distancia": containerSensor.sensor_distancia,
            "sensor_umidade": containerSensor.sensor_umidade,
            "sensor_temperatura": containerSensor.sensor_temperatura,
            "sensor_chuva": containerSensor.sensor_chuva,
            "status": status
            }
        else:
            contentor = ContentorLixo.objects.filter(id=id).first()
            data = {
            "contentor": str(contentor.id),
            "nome": contentor.nome,
            "descricao": contentor.descricao,
            "localizacao": contentor.localizacao,
            "geolocalizacao": contentor.geolocalizacao,
            "sensor_distancia": 0,
            "sensor_umidade": 0,
            "sensor_temperatura": 0,
            "sensor_chuva": 0,
            "status": False
            }

    except DadoSensor.DoesNotExist:
        contentor = ContentorLixo.objects.filter(id=id).first()
        data = {
        "contentor": str(contentor.id),
        "nome": contentor.nome,
        "descricao": contentor.descricao,
        "localizacao": contentor.localizacao,
        "geolocalizacao": contentor.geolocalizacao,
        "sensor_distancia": 0,
        "sensor_umidade": 0,
        "sensor_temperatura": 0,
        "sensor_chuva": 0,
        "status": False
        }

    return JsonResponse(data)