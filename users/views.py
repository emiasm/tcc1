from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.db import models
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, RedirectView, UpdateView

from .forms import UserRegistrationForm

User = get_user_model()

class UserCreateView(views.SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users_listar")
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


class ThirdUserUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users_listar")
    success_message = ("Usuário atualizado com sucesso!")
    template_name = "users/signup.html"


class UserUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    template_name='users/users_update_form'
    success_message = ("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user
    
user_update_view = UserUpdateView.as_view()


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "registration/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "registration/profile.html"

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

  