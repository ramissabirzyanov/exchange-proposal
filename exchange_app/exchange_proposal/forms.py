from django.forms import ModelForm

from exchange_app.exchange_proposal.models import ExchangeProposal



class ExchangeProposalCreateForm(ModelForm):

    class Meta:
        model = ExchangeProposal
        fields = ['name']
