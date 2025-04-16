from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "base.html"


class UserLoginView(SuccessMessageMixin, views.LoginView):
    template_name = "login.html"
    success_message = "Вы вошли"


class UserLogoutView(views.LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Приходите ещe')
        return self.post(request, *args, **kwargs)