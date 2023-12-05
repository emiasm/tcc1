"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView,PasswordContextMixin,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetView,PasswordChangeView
from users.views import UserCreateView,UsersListView,UserUpdateView,UsersDeleteView,filtro_users,ThirdUserUpdateView,UpdateView
from core.views import HomeView, VisitasView, LogradouroView
from imovel.views import ImovelCreateView,ImovelDeleteView,ImovelDetailView,ImovelListView, ImovelUpdateView,filtro_moradores
from visita1.views import Visita1CreateView,Visita1DeleteView,Visita1DetailView,Visita1ListView,Visita1UpdateView
from morador.views import MoradorCreateView, MoradorDeleteView, MoradorDetailView, MoradorListView,MoradorUpdateView
from visita2.views import Visita2CreateView,Visita2DeleteView,Visita2DetailView,Visita2ListView,Visita2UpdateView
from bairro.views import BairroCreateView,BairroDeleteView,BairroDetailView,BairroListView,BairroUpdateView,filtro_bairros
from rua.views import RuaCreateView,RuaDeleteView,RuaDetailView,RuaListView,RuaUpdateView,filtro_rua
from perfil.views import PerfilUpdate,ProfileView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin', admin.site.urls),
    path('', HomeView.as_view(), name='index'),
    path('visitas/', VisitasView.as_view(), name='visitas'),
    path('logradouro/', LogradouroView.as_view(), name='logradouro'),
    path('users/profile/', ProfileView.as_view(), name='users_profile'),
    path('profile/update/', PerfilUpdate.as_view(),name="editar_perfil"),

    path('users/criar', UserCreateView.as_view(), name='users_criar'),
    path('users/listar/', UsersListView.as_view(), name='users_listar'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/logout/', LogoutView.as_view(), name='logout'),
    path("users/update/<int:pk>/", UserUpdateView.as_view(), name="users_update"),
    path("users/editar/<int:pk>/", ThirdUserUpdateView.as_view(), name="users_editar"),
    path('users/remover/<int:pk>/',UsersDeleteView.as_view(), name='users_remover'),
    path('filtro_users/', filtro_users, name='filtro_users'),

    path('imovel/', ImovelCreateView.as_view(), name='imovel_criar'),
    path('imovel/detalhe/<int:pk>/',ImovelDetailView.as_view(), name='imovel_detalhe'),
    path('imovel/editar/<int:pk>/',ImovelUpdateView.as_view(), name='imovel_editar'),
    path('imovel/remover/<int:pk>/',ImovelDeleteView.as_view(), name='imovel_remover'),
    path('imovel/listar/', ImovelListView.as_view(), name='imovel_listar'),

    path('filtro_moradores/', filtro_moradores, name='filtro_moradores'),

    path('visita1/', Visita1CreateView.as_view(), name='visita1_criar'),
    path('visita1/detalhe/<int:pk>/',Visita1DetailView.as_view(), name='visita1_detalhe'),
    path('visita1/editar/<int:pk>/',Visita1UpdateView.as_view(), name='visita1_editar'),
    path('visita1/remover/<int:pk>/',Visita1DeleteView.as_view(), name='visita1_remover'),
    path('visita1/listar/', Visita1ListView.as_view(), name='visita1_listar'),

    path('visita2/', Visita2CreateView.as_view(), name='visita2_criar'),
    path('visita2/detalhe/<int:pk>/',Visita2DetailView.as_view(), name='visita2_detalhe'),
    path('visita2/editar/<int:pk>/',Visita2UpdateView.as_view(), name='visita2_editar'),
    path('visita2/remover/<int:pk>/',Visita2DeleteView.as_view(), name='visita2_remover'),
    path('visita2/listar/', Visita2ListView.as_view(), name='visita2_listar'),

    path('morador/', MoradorCreateView.as_view(), name='morador_criar'),
    path('morador/detalhe/<int:pk>/',MoradorDetailView.as_view(), name='morador_detalhe'),
    path('morador/editar/<int:pk>/',MoradorUpdateView.as_view(), name='morador_editar'),
    path('morador/remover/<int:pk>/',MoradorDeleteView.as_view(), name='morador_remover'),
    path('morador/listar/', MoradorListView.as_view(), name='morador_listar'),

    path('bairro/', BairroCreateView.as_view(), name='bairro_criar'),
    path('bairro/detalhe/<int:pk>/',BairroDetailView.as_view(), name='bairro_detalhe'),
    path('bairro/editar/<int:pk>/',BairroUpdateView.as_view(), name='bairro_editar'),
    path('bairro/remover/<int:pk>/',BairroDeleteView.as_view(), name='bairro_remover'),
    path('bairro/listar/', BairroListView.as_view(), name='bairro_listar'),
    path('filtro_bairros/', filtro_bairros, name='filtro_bairros'),

    path('rua/', RuaCreateView.as_view(), name='rua_criar'),
    path('rua/detalhe/<int:pk>/',RuaDetailView.as_view(), name='rua_detalhe'),
    path('rua/editar/<int:pk>/',RuaUpdateView.as_view(), name='rua_editar'),
    path('rua/remover/<int:pk>/',RuaDeleteView.as_view(), name='rua_remover'),
    path('rua/listar/', RuaListView.as_view(), name='rua_listar'),
    path('filtro_ruas/', filtro_rua, name='filtro_ruas'),

    path("users/password_change/", PasswordChangeView.as_view(), name="password_change"),
    path("users/password_change/done/",PasswordChangeDoneView.as_view(), name="password_change_done",),
    path("users/password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("users/password_reset/done/",PasswordResetDoneView.as_view(),name="password_reset_done",),
    path("users/reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(),name="password_reset_confirm",),
    path("users/reset/done/",PasswordResetCompleteView.as_view(),name="password_reset_complete",),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
