from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if Group.objects.filter(user=request.user).exists():
                group = Group.objects.get(user=request.user).name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('inicio')
        return wrapper_func
    return decorator