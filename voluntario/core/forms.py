from django import forms
from voluntario.core.models import Campanha

class CampanhaForm(forms.ModelForm):

    class Meta:
        model = Campanha
