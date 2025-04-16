from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet

from exchange_app.ad.models import Ad
from exchange_app.user.serializers import UserSerializer
from exchange_app.ad.forms import AdCreateForm
from exchange_app.mixins import IsUserLoggedMixin, IsAdOwnerMixin


class AdsAPIView(IsUserLoggedMixin, ModelViewSet):

    queryset = Ad.objects.all()
    serializer_class = UserSerializer


class AdCreateView(IsUserLoggedMixin, SuccessMessageMixin, CreateView):
    model = Ad
    template_name = 'ad/ad_create.html'
    form_class = AdCreateForm
    success_url = reverse_lazy('ads')
    success_message = 'Предмет успешно добавлен'


class AdListView(IsUserLoggedMixin, ListView):
    model = Ad
    template_name = 'ad/ad_list.html'
    queryset = Ad.objects.all().order_by('-created_at')

