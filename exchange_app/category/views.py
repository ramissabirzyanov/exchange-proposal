from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework.viewsets import ModelViewSet

from exchange_app.category.serializers import CategorySerializer
from exchange_app.category.models import Category
from exchange_app.category.forms import CategoryCreateForm
from exchange_app.mixins import IsUserLoggedMixin


class CategoryiesAPIView(IsUserLoggedMixin, ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(IsUserLoggedMixin, SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'category/category_create.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('category_list')
    success_message = 'Категория успешно добавлена'


class CategoryListView(IsUserLoggedMixin, ListView):
    model = Category
    template_name = 'category/category_list.html'
    queryset = Category.objects.all().order_by('id')
