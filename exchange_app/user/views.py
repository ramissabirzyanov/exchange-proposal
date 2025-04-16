from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet

from exchange_app.user.models import User
from exchange_app.user.serializers import UserSerializer
from exchange_app.user.forms import UserCreateForm
from exchange_app.mixins import IsUserLoggedMixin


class UsersAPIView(IsUserLoggedMixin, ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersListView(IsUserLoggedMixin, ListView):
    model = User
    template_name = 'user/users.html'


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('login')
    success_message = 'The user has been successfully registered'


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'