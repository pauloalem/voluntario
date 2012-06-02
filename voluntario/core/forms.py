from voluntario.core.models import Campanha

class BeneficiarioForm(forms.ModelForm):
    pass


class CampanhaForm(forms.ModelForm):

    class Meta:
        model = Campanha
