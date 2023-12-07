from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import BairroForm
from .models import Bairro

from django.shortcuts import render,  get_object_or_404
from perfil.models import Perfil
from users.models import User
from django_filters.views import FilterView
from .filters import BairroFilter

from users.permissions import ACEPermission,ACSPermission,AdminPermission

class BairroListView(LoginRequiredMixin, FilterView):
  model = Bairro
  paginate_by=5
  filterset_class = BairroFilter
  template_name = "bairro/bairros.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
  

class BairroDetailView(LoginRequiredMixin, generic.DetailView):
  model = Bairro
  template_name = "bairro/bairro_detalhe.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class BairroCreateView(AdminPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Bairro
  form_class = BairroForm
  success_url = reverse_lazy("bairro_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "bairro/form.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
  
class BairroDeleteView(AdminPermission,LoginRequiredMixin, generic.DeleteView):
  model = Bairro
  success_url = reverse_lazy("bairro_listar")
  template_name = "bairro/bairro_confirm_delete.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
  
class BairroUpdateView(AdminPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Bairro
  form_class = BairroForm
  success_url = reverse_lazy("bairro_listar")
  success_message= 'Alterações salvas!'
  template_name = "bairro/form.html"
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

def filtro_bairros(request):
    termo_bairro = request.GET.get('termo_bairro', '')
    ordenacao = request.GET.get('ordenacao', 'mais_recente')  # Padrão para ordenação mais recente

    if ordenacao == 'mais_antigo':
        bairros = Bairro.objects.order_by('data_adicao')
    else:
        bairros = Bairro.objects.order_by('-data_adicao')

    if termo_bairro:
        bairros = bairros.filter(nome__icontains=termo_bairro)


    return render(request, 'bairro/filter_bairro.html', {
        'bairros': bairros,
        'termo_bairro': termo_bairro,
        'ordenacao': ordenacao,
    })
  



