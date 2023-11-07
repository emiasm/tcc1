from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import Visita1Form
from .models import Visita1

class Visita1ListView(LoginRequiredMixin, generic.ListView):
    model = Visita1
    # paginate_by=3
    template_name = "visita1/visitas.html"

class Visita1DetailView(LoginRequiredMixin, generic.DetailView):
    model = Visita1
    template_name = "visita1/visita1_detalhe.html"

class Visita1CreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Visita1
  form_class = Visita1Form
  success_url = reverse_lazy("visita1_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "visita1/form.html"
  
class Visita1DeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Visita1
  success_url = reverse_lazy("visita1_listar")
  template_name = "visita1/visita1_confirm_delete.html"
  
class Visita1UpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Visita1
  form_class = Visita1Form
  success_url = reverse_lazy("visita1_listar")
  success_message= 'Alterações salvas!'
  template_name = "visita1/form.html"


