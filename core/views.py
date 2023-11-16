from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from users.permissions import AdminPermission
from users.models import User

class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context
    
class VisitasView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/visitas.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context

class LogradouroView(LoginRequiredMixin, generic.TemplateView):
    template_name = "pages/logradouro.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        return context