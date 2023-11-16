from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import Visita2Form
from .models import Visita2
from .filters import Visita2Filter
from django_filters.views import FilterView

class Visita2ListView(LoginRequiredMixin, FilterView):
    model = Visita2
    # paginate_by=3
    filterset_class = Visita2Filter
    template_name = "visita2/visitas.html"

class Visita2DetailView(LoginRequiredMixin, generic.DetailView):
    model = Visita2
    template_name = "visita2/visita2_detalhe.html"

class Visita2CreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Visita2
  form_class = Visita2Form
  success_url = reverse_lazy("visita2_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "visita2/form.html"
  
class Visita2DeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Visita2
  success_url = reverse_lazy("visita2_listar")
  template_name = "visita2/visita2_confirm_delete.html"
  
class Visita2UpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Visita2
  form_class = Visita2Form
  success_url = reverse_lazy("visita2_listar")
  success_message= 'Alterações salvas!'
  template_name = "visita2/form.html"


