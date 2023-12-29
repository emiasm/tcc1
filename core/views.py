from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic
from users.permissions import AdminPermission
from users.models import User
from perfil.models import Perfil
from visita2.models import Visita2
import json
from visita1.models import Visita1
import matplotlib.pyplot as plt
from django.db.models.functions import TruncMonth
import os
import io
from django.db.models import Sum, F, ExpressionWrapper, IntegerField, Q, Count
from django.db import models
from django.shortcuts import get_object_or_404
import urllib
from django.http import HttpResponse
from collections import defaultdict
from django.http import JsonResponse


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        # Código para o gráfico de barras por bairro
        bairros_distintos = Visita2.objects.values_list('imovel__bairro__nome', flat=True).distinct()
        contagens_por_bairro = defaultdict(lambda: defaultdict(int))

        for bairro in bairros_distintos:
            visitas_por_bairro = Visita2.objects.filter(imovel__bairro__nome=bairro)
            contagens_por_bairro[bairro]['total_dengue'] = visitas_por_bairro.filter(dengue=True).count()
            contagens_por_bairro[bairro]['total_dengue_hemorragica'] = visitas_por_bairro.filter(dengue_hemorragica=True).count()
            contagens_por_bairro[bairro]['total_zika'] = visitas_por_bairro.filter(zika=True).count()
            contagens_por_bairro[bairro]['total_chikungunya'] = visitas_por_bairro.filter(chikungunya=True).count()

        bairros = list(contagens_por_bairro.keys())
        total_dengue = [contagens_por_bairro[bairro]['total_dengue'] for bairro in bairros]
        total_dengue_hemorragica = [contagens_por_bairro[bairro]['total_dengue_hemorragica'] for bairro in bairros]
        total_zika = [contagens_por_bairro[bairro]['total_zika'] for bairro in bairros]
        total_chikungunya = [contagens_por_bairro[bairro]['total_chikungunya'] for bairro in bairros]

        context['bairros'] = bairros
        context['total_dengue'] = total_dengue
        context['total_dengue_hemorragica'] = total_dengue_hemorragica
        context['total_zika'] = total_zika
        context['total_chikungunya'] = total_chikungunya
        
        # Cálculo da contagem de cada tipo de foco
        total_visitas = Visita1.objects.count()
        contagem_focos = (
            Visita1.objects.values('focos')
            .annotate(total=Count('focos'))
            .order_by()
        )

        # Cálculo da porcentagem de cada tipo de foco
        porcentagens = {}
        for item in contagem_focos:
            porcentagens[item['focos']] = (item['total'] / total_visitas) * 100

        context['porcentagens'] = porcentagens

        # Código para outras informações
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = get_object_or_404(Perfil, usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        # Código para gráfico de contagem mensal
        data = Visita2.objects.annotate(
            month=TruncMonth('data_visita')
        ).values('month').annotate(
            dengue=Count('id', filter=Q(dengue=True)),
            dengue_hemorragica=Count('id', filter=Q(dengue_hemorragica=True)),
            zika=Count('id', filter=Q(zika=True)),
            chikungunya=Count('id', filter=Q(chikungunya=True)),
        ).order_by('month')

        labels = [d['month'].strftime('%b %Y') for d in data]
        data_dengue = [int(d['dengue']) for d in data]
        data_dengue_hemorragica = [int(d['dengue_hemorragica']) for d in data]
        data_zika = [int(d['zika']) for d in data]
        data_chikungunya = [int(d['chikungunya']) for d in data]

        context['labels'] = labels
        context['data_dengue'] = data_dengue
        context['data_dengue_hemorragica'] = data_dengue_hemorragica
        context['data_zika'] = data_zika
        context['data_chikungunya'] = data_chikungunya

        
       
        # Código para os outros gráficos...
        # ... (códigos dos outros gráficos)

        # Código para o gráfico de pizza
        visitas = Visita2.objects.all()
        dengue_count = visitas.filter(dengue=True).count()
        dengue_hemorragica_count = visitas.filter(dengue_hemorragica=True).count()
        zika_count = visitas.filter(zika=True).count()
        chikungunya_count = visitas.filter(chikungunya=True).count()

        sizes = [dengue_count, dengue_hemorragica_count, zika_count, chikungunya_count]
        labels = ['Dengue', 'Dengue Hemorrágica', 'Zika', 'Chikungunya']
        colors = ["#022F32", "#02565B", "#0E7981", "#2C9EA6"]

        total = sum(sizes)
        percentages = [(size / total) * 100 for size in sizes]

        chart_data = {
            'labels': labels,
            'percentages': percentages,
            'sizes': sizes,
            'colors': colors,
        }

        context['chart_data'] = chart_data

        return context


    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    


class VisitasView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/visitas.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(
            Perfil, usuario=self.request.user)
        context["users_number"] = User.objects.exclude(
            is_superuser=True).exclude(email="deleted").count()

        return context


class LogradouroView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/logradouro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(
            Perfil, usuario=self.request.user)
        context["users_number"] = User.objects.exclude(
            is_superuser=True).exclude(email="deleted").count()

        return context

