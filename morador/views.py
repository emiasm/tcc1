from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404
from perfil.models import Perfil
from users.models import User

from .forms import MoradorForm
from .models import Morador

from users.permissions import ACSADMINPermission

class MoradorListView(LoginRequiredMixin, generic.ListView):
    model = Morador
    # paginate_by=3
    template_name = "morador/moradores.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
    
    

class MoradorDetailView(ACSADMINPermission, LoginRequiredMixin, generic.DetailView):
    model = Morador
    template_name = "morador/morador_detalhe.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class MoradorCreateView(ACSADMINPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Morador
  form_class = MoradorForm
  success_url = reverse_lazy("imovel_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "morador/form.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
  

class MoradorDeleteView(ACSADMINPermission,LoginRequiredMixin, generic.DeleteView):
  model = Morador
  success_url = reverse_lazy("imovel_listar")
  template_name = "morador/morador_confirm_delete.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
  
class MoradorUpdateView(ACSADMINPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Morador
  form_class = MoradorForm
  success_url = reverse_lazy("imovel_listar")
  success_message= 'Alterações salvas!'
  template_name = "morador/form.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
