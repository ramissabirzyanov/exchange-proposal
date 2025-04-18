from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action


from exchange_app.user.models import User
from exchange_app.user.serializers import UserSerializer, UserCreateSerializer
from exchange_app.user.forms import UserCreateForm
from exchange_app.mixins import IsUserLoggedMixin, UserAccessPermission


class UsersAPIViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserAccessPermission]

    def get_serializer_class(self):
        if self.action == 'create_user':
            return UserCreateSerializer
        return UserSerializer

    @action(detail=False, methods=['post'], url_path='create')
    def create_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('login')
    success_message = 'The user has been successfully registered'


class UserDetailView(IsUserLoggedMixin, DetailView):
    model = User
    template_name = 'user/user_detail.html'
