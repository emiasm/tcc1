from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import BairroForm
from .models import Bairro
from django.shortcuts import render

class BairroListView(LoginRequiredMixin, generic.ListView):
  model = Bairro
  # paginate_by=3
  template_name = "bairro/bairros.html"
  

class BairroDetailView(LoginRequiredMixin, generic.DetailView):
  model = Bairro
  template_name = "bairro/bairro_detalhe.html"

class BairroCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Bairro
  form_class = BairroForm
  success_url = reverse_lazy("bairro_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "bairro/form.html"
  
class BairroDeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Bairro
  success_url = reverse_lazy("bairro_listar")
  template_name = "bairro/bairro_confirm_delete.html"
  
class BairroUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Bairro
  form_class = BairroForm
  success_url = reverse_lazy("bairro_listar")
  success_message= 'Alterações salvas!'
  template_name = "bairro/form.html"

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


