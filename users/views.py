from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from .forms import UserRegistrationForm

User = get_user_model()

class UserCreateView(views.SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("index")
    success_message = "Usuário cadastrado com sucesso!"
    template_name = "users/signup.html"

class UsersListView(LoginRequiredMixin, generic.ListView):
    model = User
    paginate_by = 5
    ordering = ["name"]
    template_name = "users/users.html"

class UsersDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("users_listar")
    template_name = "users/users_confirm_delete.html"


def filtro_users(request):
    termo_users = request.GET.get('termo_users', '')
    ordenacao = request.GET.get('ordenacao', 'mais_recente')  # Padrão para ordenação mais recente

    if ordenacao == 'mais_antigo':
        users = User.objects.order_by('data_adicao')
    else:
        users = User.objects.order_by('-data_adicao')

    if termo_users:
        users = users.filter(username__icontains=termo_users)


    return render(request, 'users/filter_users.html', {
        'users': users,
        'termo_users': termo_users,
        'ordenacao': ordenacao,
    })

  