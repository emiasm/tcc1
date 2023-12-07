from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import MoradorForm
from .models import Morador

from users.permissions import ACEPermission,ACSPermission,AdminPermission

class MoradorListView(LoginRequiredMixin, generic.ListView):
    model = Morador
    # paginate_by=3
    template_name = "morador/moradores.html"
    
    

class MoradorDetailView(ACSPermission,AdminPermission,ACEPermission, LoginRequiredMixin, generic.DetailView):
    model = Morador
    template_name = "morador/morador_detalhe.html"

class MoradorCreateView(ACSPermission,AdminPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Morador
  form_class = MoradorForm
  success_url = reverse_lazy("imovel_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "morador/form.html"

class MoradorDeleteView(ACSPermission,AdminPermission,LoginRequiredMixin, generic.DeleteView):
  model = Morador
  success_url = reverse_lazy("imovel_listar")
  template_name = "morador/morador_confirm_delete.html"
  
class MoradorUpdateView(ACSPermission,AdminPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Morador
  form_class = MoradorForm
  success_url = reverse_lazy("imovel_listar")
  success_message= 'Alterações salvas!'
  template_name = "morador/form.html"
