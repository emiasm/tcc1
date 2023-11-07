from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import RuaForm
from .models import Rua
from django.shortcuts import render



class RuaListView(LoginRequiredMixin, generic.ListView):
    model = Rua
    # paginate_by=3
    template_name = "rua/ruas.html"

class RuaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Rua
    template_name = "rua/rua_detalhe.html"

class RuaCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Rua
  form_class = RuaForm
  success_url = reverse_lazy("rua_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "rua/form.html"

class RuaDeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Rua
  success_url = reverse_lazy("rua_listar")
  template_name = "rua/rua_confirm_delete.html"
  
class RuaUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Rua
  form_class = RuaForm
  success_url = reverse_lazy("rua_listar")
  success_message= 'Alterações salvas!'
  template_name = "rua/form.html"

# def filtro_rua(request):
#     termo_rua = request.GET.get('termo_rua', '')
#     ruas = Rua.objects.order_by('nome')

#     if termo_rua:
#         ruas = ruas.filter(nome__icontains=termo_rua)

#     return render(request, 'rua/filter_rua.html', {'ruas': ruas, 'termo_rua': termo_rua})

def filtro_rua(request):
    termo_rua = request.GET.get('termo_rua', '')
    ordenacao = request.GET.get('ordenacao', 'mais_recente')  # Padrão para ordenação mais recente

    if ordenacao == 'mais_antigo':
        ruas = Rua.objects.order_by('data_adicao')
    else:
        ruas = Rua.objects.order_by('-data_adicao')

    if termo_rua:
        ruas = ruas.filter(nome__icontains=termo_rua)


    return render(request, 'rua/filter_rua.html', {
        'ruas': ruas,
        'termo_rua': termo_rua,
        'ordenacao': ordenacao,
    })
