# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from voluntario.core.models import UsuarioPerfil, Area, Estado, Cidade, Pais
from voluntario.facebook.models import FacebookProfile

from django.forms.fields import DateField, MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.extras.widgets import SelectDateWidget

class EnderecoForm(forms.Form):
    endereco = forms.CharField(max_length=225, required=True)
    numero = forms.IntegerField(required=True)
    complemento = forms.CharField(max_length=225, required=False)
    
    estados = [(e.nome, e.sigla) for e in Estado.objects.all()]
    estado = forms.ChoiceField(label=u'Estado', choices=estados)
    
    cidades = [(c.nome, c.nome) for c in Cidade.objects.all()]
    cidade = forms.ChoiceField(label=u'Cidade', choices=cidades)
    
    paises = [(p.nome, p.nome) for p in Pais.objects.all()]
    pais = forms.ChoiceField(label=u'País', choices=paises)

class VoluntarioForm(EnderecoForm):
    nome = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)
    senha = forms.CharField(widget=forms.PasswordInput(render_value=False), required=True)
    
    #list_areas = [(a.nome, a.nome) for a in Area.objects.all()]
    #areas = forms.MultipleChoiceField(label=u'Áreas', required=False,
    #    widget=CheckboxSelectMultiple, choices=list_areas)
    
    autorizacao_email = forms.BooleanField( required=False, \
                                            label="Aceito receber e-mails do voluntar.io.", \
                                            initial=True )

    def __init__(self, *args, **kwargs):
        super(VoluntarioForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['nome', 'email', 'senha', 'endereco', 'numero', 'complemento', 'estado', 'cidade', 'pais', 'autorizacao_email']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError(u'Este e-mail já está cadastrado no voluntar.io.')
            
        return email
    
    def save(self, access_token=None, fb_profile=None):
        
        # para gerar um código aleatório que será temporariamente o username dos usuários
        import md5
        m = md5.new()
        
        if access_token and fb_profile:
            m.update(fb_profile['email'])
            m.update(fb_profile['id'])
            username = m.hexdigest()[-30:]

            user = User.objects.create_user(username, fb_profile['email'])
                    
            user.set_password(self.cleaned_data.get('senha'))
            
            user.first_name = self.cleaned_data.get('nome')
            user.save()
            
            # Create the FacebookProfile
            fb_user = FacebookProfile(user=user, facebook_id=fb_profile['id'], access_token=access_token)
            fb_user.save()
                
        else:
            email = self.cleaned_data.get('email')
            
            m.update(email)
            username = m.hexdigest()[-30:]
             
            user = User.objects.create_user(username, email)
            
            user.set_password(self.cleaned_data.get('senha'))
            
            user.first_name = self.cleaned_data['nome']
            user.save()
            
        perfil = UsuarioPerfil()
        perfil.usuario = user
        #perfil.areas = self.cleaned_data.get('areas', '')
        perfil.aceita_email = int( self.cleaned_data.get('autorizacao_email', 1) )
        perfil.save()
        
        return user
    
class VoluntarioEdicaoForm(EnderecoForm):
    nome = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=255, required=True)
    senha = forms.CharField(widget=forms.PasswordInput(render_value=False), required=True)
    
    list_areas = [(a.nome, a.nome) for a in Area.objects.all()]
    areas = forms.MultipleChoiceField(label=u'Áreas', required=False,
        widget=CheckboxSelectMultiple, choices=list_areas)
    
    gender_choices = [(u'', 'Selecione o sexo'), \
                      (u'F', 'Feminino'), \
                      (u'M', 'Masculino')]
    
    sexo = forms.ChoiceField( label="Sexo", \
                               choices=gender_choices, \
                               initial=u'', \
                               required=False )
    
    autorizacao_email = forms.BooleanField( required=False, \
                                            label="Aceito receber e-mails do voluntar.io.", \
                                            initial=True )
    
    def __init__(self, *args, **kwargs):
        super(VoluntarioEdicaoForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['readonly'] = True
    
    def update(self, user):
        
        try:
            user.first_name = self.cleaned_data.get('nome')
            
            nova_senha = self.cleaned_data.get('senha')
            if nova_senha:
                user.set_password(nova_senha)
                
            user.save()
            
            user_profile = UsuarioPerfil.objects.get(usuario=user)
            user_profile.sexo = self.cleaned_data.get('sexo')
            user_profile.notificacao = self.cleaned_data.get('areas', 'mensal')
            user_profile.aceita_email = int( self.cleaned_data.get('autorizacao_email', 1) )
            
            user_profile.save()
            
            return True
        except:
            return False
