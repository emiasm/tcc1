from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import Visita2Form
from .models import Visita2
from .filters import Visita2Filter
from django_filters.views import FilterView
from django.shortcuts import render,  get_object_or_404
from perfil.models import Perfil
from users.models import User

class Visita2ListView(LoginRequiredMixin, FilterView):
    model = Visita2
    paginate_by=10
    filterset_class = Visita2Filter
    template_name = "visita2/visitas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class Visita2DetailView(LoginRequiredMixin, generic.DetailView):
    model = Visita2
    template_name = "visita2/visita2_detalhe.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class Visita2CreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Visita2
  form_class = Visita2Form
  success_url = reverse_lazy("visita2_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "visita2/form.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
  
class Visita2DeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Visita2
  success_url = reverse_lazy("visita2_listar")
  template_name = "visita2/visita2_confirm_delete.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
  
class Visita2UpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Visita2
  form_class = Visita2Form
  success_url = reverse_lazy("visita2_listar")
  success_message= 'Alterações salvas!'
  template_name = "visita2/form.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context


