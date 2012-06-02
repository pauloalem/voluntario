# -*- coding: utf-8 -*-
import md5

from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from voluntario.core.forms import CampanhaForm
from voluntario.core.models import Campanha, Voluntario
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth import authenticate, login
from django.conf import settings
from django import forms
from django.core.mail import send_mail
from django.contrib.auth.models import User

from voluntario.facebook import FacebookComponent

from voluntario.core.models import *
from voluntario.core.forms import VoluntarioForm, VoluntarioEdicaoForm

from time import time

import logging

@csrf_exempt
def user_login(request):
    if request.method == "POST" and request.is_ajax() and request.user.is_anonymous():
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(email=email, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                
                response_dict = {'status': 'success', 'msg': 'Login efetuado com sucesso.'}
                response_json = simplejson.dumps(response_dict)
                response = HttpResponse(response_json, 'application/javascript')
                    
            else:
                response_dict = {'status': 'error', 'msg': 'Usuário inativo.'}
                response_json = simplejson.dumps(response_dict)
                response = HttpResponse(response_json, 'application/javascript')
        else:
            response_dict = {'status': 'error', 'msg': 'E-mail ou senha inválido.'}
            response_json = simplejson.dumps(response_dict)
            response = HttpResponse(response_json, 'application/javascript')
    else:
        response = HttpResponse(simplejson.dumps({}), 'application/javascript')
        
    return response

@csrf_exempt
def remember_password(request):
    if request.method == "POST" and request.is_ajax() and request.user.is_anonymous():
        email = request.POST.get('email')
        
        try:
            user = User.objects.get(email=email)
            
            gen_senha = '%s%s' % (user.email, str(time()))
            
            m = md5.new()
            m.update(gen_senha)
            nova_senha = m.hexdigest()[:6]
            
            subject = u'Sua nova senha no Voluntar.io'
            message = u"Olá %s,\n\nSua nova senha no Voluntar.io é: %s" % (user.first_name, str(nova_senha))
            
            if send_mail(subject.encode('utf8'), message.encode('utf8'), recipient_list=[user.email], from_email="voluntar.io@gmail.com"):
                
                user.set_password(nova_senha)
                user.save()
                
                response_dict = {'status': 'success', 'msg': 'Você irá receber sua nova senha no seu e-mail de cadastro.'}
                response_json = simplejson.dumps(response_dict)
                response = HttpResponse(response_json, 'application/javascript')
        except Exception, e:
            
            logging.info("[voluntario.core.views.remember_password:85] Erro no lembrar senha: %s" % e.message)
            
            response_dict = {'status': 'error', 'msg': 'Este e-mail ainda não foi cadastrado.'}
            response_json = simplejson.dumps(response_dict)
            response = HttpResponse(response_json, 'application/javascript')
    else:
        response = HttpResponse(simplejson.dumps({}), 'application/javascript')
        
    return response

def user_register(request, type):
    context = RequestContext(request)

    initial = {}
    fb_cadastro = False
    
    access_token = request.session.get('fb_access_token')
    fb_profile = None
    
    if access_token:
        fb_component = FacebookComponent(app_id=settings.FACEBOOK_APP_ID, app_secret=settings.FACEBOOK_APP_SECRET)
        
        fb_profile = fb_component.get_facebook_profile(access_token)
        
        if fb_profile:
            initial['nome'] = fb_profile.get('name', '')
            initial['email'] = fb_profile.get('email', '')
            fb_cadastro = True
            
    if request.method == "POST":
        for key in request.POST.keys():
            initial.update({key: request.POST.get(key)})
            
        if type == 'voluntario':
            user_form = VoluntarioForm(initial)
        else:
            user_form = BeneficiarioForm(initial)
    else:
        if type == 'voluntario':
            user_form = VoluntarioForm(initial=initial)
        else:
            user_form = BeneficiarioForm(initial=initial)
        
    user_form.fb_cadastro = fb_cadastro
        
    if access_token and fb_profile:
        user_form.fields['nome'].widget.attrs['disabled'] = True
        user_form.fields['nome'].widget.attrs['required'] = False
        user_form.fields['email'].widget.attrs['disabled'] = True
        user_form.fields['email'].widget.attrs['required'] = False
        
    import ipdb;ipdb.set_trace()
    if request.method == "POST":
        if user_form.is_valid():
            user = user_form.save(access_token=access_token, fb_profile=fb_profile)
            if user:
                user = authenticate(email=user_form.cleaned_data.get('email'), password=user_form.cleaned_data.get('senha'))
                if user:
                    login(request, user)
                    return redirect(reverse('dashboard'))
    
    context.update({'form': user_form, 'type': type})
    
    return render_to_response('cadastro.html', context)

def user_edit(request, type):
    if request.user.is_anonymous():
        return HttpResponseRedirect(reverse('homepage'))
    
    context = RequestContext(request)
    
    if request.method == "POST":
        form = VoluntarioEdicaoForm(request.POST)
        if form.is_valid():
            if form.update(request.user):
                context.update({'feedback': 'Sua conta foi atualizada com sucesso.'})
            else:
                context.update({'feedback': 'Ocorreu um erro ao tentar atualizar sua conta.'})
    else:
        try:
            user_perfil = request.user.user_perfil.get()
        except:
            user_perfil = UsuarioPerfil()
            user_perfil.usuario=request.user
            user_perfil.areas=[]
            user_perfil.aceita_email=1
            user_perfil.save()
        
        initial = {
                   'nome': request.user.first_name, \
                   'email': request.user.email, \
                   'areas': user_perfil.areas, \
                   'sexo': user_perfil.sexo if user_perfil.sexo else '', \
                   'autorizacao_email': user_perfil.aceita_email \
                   }
        
        form = VoluntarioEdicaoForm(initial=initial)
        
        
    context.update({'form': form})
    
    return render_to_response('edicao_perfil.html', context)

def perfil(request, username):
    pass

def facebook_setup(request):
    context = RequestContext(request)
    
    token = request.GET.get('code')
    
    fb_component = FacebookComponent(app_id=settings.FACEBOOK_APP_ID, app_secret=settings.FACEBOOK_APP_SECRET)
    
    access_token = fb_component.get_access_token(code=token, redirect_uri=request.build_absolute_uri('/facebook/authentication_callback'))
    
    request.session['fb_access_token'] = access_token
    
    return HttpResponseRedirect(reverse('user_register'))

def index(request):
    return render(request, "index.html", {})

def dashboard(request, voluntario_id):
    voluntario = Voluntario.objects.get(id=voluntario_id)
    return render(request, "dashboard.html", {'voluntario':voluntario})

def beneficiario(request):
    return render(request, "beneficiario.html", {})

def campanha(request):
    if request.method == "POST":
        form = CampanhaForm(request.POST)
        if form.is_valid():
            return redirect('campanha-show', id_campanha=form.id)
    else:
        form = CampanhaForm()
    return render(request, "campanha.html", {"form": form})

def campanha_show(request, id_campanha):
    campanha = get_object_or_404(Campanha, pk=id_campanha)
    return render(request, "campanha_show.html", {"campanha": campanha})
