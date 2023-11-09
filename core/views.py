from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from users.permissions import AdminPermission


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/home.html"

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "registration/profile.html"

class VisitasView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/visitas.html"

class LogradouroView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/logradouro.html"