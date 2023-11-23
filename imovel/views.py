from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdminPermission
from .forms import ImovelForm
from .models import Imovel
from django.shortcuts import render
from django_filters.views import FilterView
from .filters import ImovelFilter
from users.models import User

class ImovelListView(LoginRequiredMixin, FilterView):
    model = Imovel
    # paginate_by=3
    filterset_class = ImovelFilter
    template_name = "imovel/imoveis.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class ImovelDetailView(LoginRequiredMixin, generic.DetailView):
    model = Imovel
    template_name = "imovel/imovel_detalhe.html"

class ImovelCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Imovel
  form_class = ImovelForm
  success_url = reverse_lazy("imovel_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "imovel/form.html"
  
class ImovelDeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Imovel
  success_url = reverse_lazy("imovel_listar")
  template_name = "imovel/imovel_confirm_delete.html"
  
class ImovelUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Imovel
  form_class = ImovelForm
  success_url = reverse_lazy("imovel_listar")
  success_message= 'Alterações salvas!'
  template_name = "imovel/form.html"


def filtro_moradores(request):
    termo_morador = request.GET.get('termo_morador', '')
    ordenacao = request.GET.get('ordenacao', 'mais_recente')  # Padrão para ordenação mais recente

    if ordenacao == 'mais_antigo':
        moradores = Imovel.objects.order_by('data_adicao')
    else:
        moradores = Imovel.objects.order_by('-data_adicao')

    if termo_morador:
        moradores = moradores.filter(morador__icontains=termo_morador)


    return render(request, 'imovel/filter_imovel.html', {
        'moradores': moradores,
        'termo_morador': termo_morador,
        'ordenacao': ordenacao,
    })