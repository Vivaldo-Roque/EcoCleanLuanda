from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from usuarios.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['admin'])
def dashboard(request):

    usuario = request.user

    context = {'usuario': usuario}

    return render(request, "dashboard.html", context=context)
