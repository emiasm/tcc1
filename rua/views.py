from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import RuaForm
from .models import Rua
from django.shortcuts import render,  get_object_or_404
from perfil.models import Perfil
from users.models import User
from django_filters.views import FilterView
from .filters import RuaFilter


from users.permissions import AdminPermission


class RuaListView(LoginRequiredMixin, FilterView):
    model = Rua
    filterset_class = RuaFilter
    paginate_by=10 
    template_name = "rua/ruas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class RuaDetailView(AdminPermission,LoginRequiredMixin, generic.DetailView):
    model = Rua
    template_name = "rua/rua_detalhe.html"

class RuaCreateView(AdminPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Rua
  form_class = RuaForm
  success_url = reverse_lazy("rua_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "rua/form.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class RuaDeleteView(AdminPermission,LoginRequiredMixin, generic.DeleteView):
  model = Rua
  success_url = reverse_lazy("rua_listar")
  template_name = "rua/rua_confirm_delete.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
  
class RuaUpdateView(AdminPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Rua
  form_class = RuaForm
  success_url = reverse_lazy("rua_listar")
  success_message= 'Alterações salvas!'
  template_name = "rua/form.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context




