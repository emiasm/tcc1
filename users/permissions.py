from django.contrib.auth.mixins import UserPassesTestMixin


class AdminPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Administrador"):
            return True
        return False



class ACEPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Agente de Endemias"):
            return True
        return False

from django.contrib.auth.mixins import UserPassesTestMixin


class ACSPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Agente de Saúde"):
            return True
        return False