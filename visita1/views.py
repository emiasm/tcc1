from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import Visita1Form
from .models import Visita1
from .filters import Visita1Filter
from django_filters.views import FilterView
from django.shortcuts import render,  get_object_or_404
from perfil.models import Perfil
from users.models import User

from users.permissions import ACEAdminPermission,ACSACEADMINPermission
   

class Visita1ListView(LoginRequiredMixin, FilterView):
    model = Visita1
    paginate_by=10
    filterset_class = Visita1Filter
    template_name = "visita1/visitas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class Visita1DetailView(ACSACEADMINPermission,LoginRequiredMixin, generic.DetailView):
    model = Visita1
    template_name = "visita1/visita1_detalhe.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class Visita1CreateView(ACEAdminPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Visita1
  form_class = Visita1Form
  success_url = reverse_lazy("visita1_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "visita1/form.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
  
class Visita1DeleteView(ACEAdminPermission,LoginRequiredMixin, generic.DeleteView):
  model = Visita1
  success_url = reverse_lazy("visita1_listar")
  template_name = "visita1/visita1_confirm_delete.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
  
class Visita1UpdateView(ACSACEADMINPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Visita1
  form_class = Visita1Form
  success_url = reverse_lazy("visita1_listar")
  success_message= 'Alterações salvas!'
  template_name = "visita1/form.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context


