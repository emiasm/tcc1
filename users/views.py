from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.db import models
from django.forms.forms import BaseForm
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from perfil.models import Perfil
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, RedirectView, UpdateView
from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView,PasswordContextMixin,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetView
from .forms import UserRegistrationForm
from django_filters.views import FilterView
from .filters import UsersFilter

from users.permissions import ACEPermission,ACSPermission,AdminPermission


User = get_user_model()

class UserCreateView(AdminPermission,views.SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users_listar")
    success_message = "Usuário cadastrado com sucesso!"
    template_name = "users/signup.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

    def form_valid(self, form):
        url = super().form_valid(form)

        Perfil.objects.create(usuario=self.object)

        return url

    def form_invalid(self, form ):
        print(form.errors)
        return super().form_invalid(form)


class UsersListView(AdminPermission,LoginRequiredMixin, FilterView):
    model = User
    filterset_class = UsersFilter
    paginate_by = 4
    ordering = ["name"]
    template_name = "users/users.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class UsersDeleteView(AdminPermission, LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("users_listar")
    template_name = "users/users_confirm_delete.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context


class ThirdUserUpdateView(AdminPermission,LoginRequiredMixin, views.SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users_listar")
    success_message = ("Usuário atualizado com sucesso!")
    template_name = "users/signup.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class UserUpdateView(AdminPermission,LoginRequiredMixin, views.SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users_listar")
    success_message = ("Usuário atualizado com sucesso!")
    template_name = "users/signup.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context




class UserDetailView(AdminPermission,LoginRequiredMixin, DetailView):
    model = User
    slug_field = "id"
    slug_url_kwarg = "id"
    template_name = "registration/profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

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

