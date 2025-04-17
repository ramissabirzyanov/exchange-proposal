from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet

from exchange_app.ad.models import Ad
from exchange_app.ad.serializers import AdSerializer
from exchange_app.ad.forms import AdCreateForm
from exchange_app.mixins import IsUserLoggedMixin, IsAdOwnerMixin


class AdsAPIView(IsUserLoggedMixin, ModelViewSet):

    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreateView(IsUserLoggedMixin, SuccessMessageMixin, CreateView):
    model = Ad
    template_name = 'ad/ad_create.html'
    form_class = AdCreateForm
    success_url = reverse_lazy('ad_list')
    success_message = 'Предмет успешно добавлен'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AdListView(IsUserLoggedMixin, ListView):
    model = Ad
    template_name = 'ad/ad_list.html'
    queryset = Ad.objects.all().order_by('-created_at')

