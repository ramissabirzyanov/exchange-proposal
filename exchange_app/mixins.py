from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.permissions import BasePermission


class NoPermissionHandleMixin:
    permission_denied_message = ''
    permission_denied_url = reverse_lazy('main_page')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(self.permission_denied_url)


class IsUserLoggedMixin(NoPermissionHandleMixin, LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = 'Пожалуйста зарегистрируйтесь!'
        self.permission_denied_url = reverse_lazy('login')
        return super().dispatch(request, *args, **kwargs)


class IsAdOwnerMixin(NoPermissionHandleMixin, UserPassesTestMixin):
    def test_func(self):
        ad = self.get_object()
        return self.request.user.id == ad.owner_id

    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = "Не достаточно прав!"
        self.permission_denied_url = reverse_lazy('users')
        return super().dispatch(request, *args, **kwargs)


class UserAccessPermission(BasePermission):
    message = "Недостаточно прав"

    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action in ['list', 'retrieve']:
            return True
        return obj == request.user
