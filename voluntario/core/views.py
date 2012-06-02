from django.shortcuts import render
from voluntario.core.models import Voluntario

def index(request):
    return render(request, "index.html", {})

def dashboard(request, voluntario_id):
    voluntario = Voluntario.objects.get(id=voluntario_id)
    return render(request, "dashboard.html", {'voluntario':voluntario})

def cadastrar_beneficiario(request):
    return render(request, "cadastrar_beneficiario.html", {})