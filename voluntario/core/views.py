from django.shortcuts import render, redirect, get_object_or_404
from voluntario.core.forms import CampanhaForm
from voluntario.core.models import Campanha, Voluntario

def index(request):
    return render(request, "index.html", {})

def dashboard(request, voluntario_id):
    voluntario = Voluntario.objects.get(id=voluntario_id)
    return render(request, "dashboard.html", {'voluntario':voluntario})

def campanha(request):
    if request.method == "POST":
        form = CampanhaForm(request.POST)
        if form.is_valid():
            campanha = form.save(commit=True)
            return redirect('campanha-show', id_campanha=campanha.id)
    else:
        form = CampanhaForm()
    return render(request, "campanha.html", {"form": form})

def campanha_show(request, id_campanha):
    campanha = get_object_or_404(Campanha, pk=id_campanha)
    return render(request, "campanha_show.html", {"campanha": campanha})
