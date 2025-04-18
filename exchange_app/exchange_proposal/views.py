from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework.viewsets import ModelViewSet

from exchange_app.exchange_proposal.serializers import ExchangeProposalSeliazer
from exchange_app.exchange_proposal.models import ExchangeProposal
from exchange_app.exchange_proposal.forms import ExchangeProposalCreateForm
from exchange_app.mixins import IsUserLoggedMixin


class EP_APIView(IsUserLoggedMixin, ModelViewSet):
    queryset = ExchangeProposal.objects.all()
    serializer_class = ExchangeProposalSeliazer


class EP_CreateView(IsUserLoggedMixin, SuccessMessageMixin, CreateView):
    model = ExchangeProposal
    template_name = 'exchange_proposal/ep_create.html'
    form_class = ExchangeProposalCreateForm
    success_url = reverse_lazy('ep_list')
    success_message = ' успешно добавлена'


class EP_ListView(IsUserLoggedMixin, ListView):
    model = ExchangeProposal
    template_name = 'exchange_proposal/ep_list.html'
    queryset = ExchangeProposal.objects.all().order_by('id')
