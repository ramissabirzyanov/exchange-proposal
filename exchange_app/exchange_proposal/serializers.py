from rest_framework import serializers
from exchange_app.exchange_proposal.models import ExchangeProposal


class ExchangeProposalSeliazer(serializers.ModelSerializer):
    
    class Meta:
        model = ExchangeProposal
        fields = '__all__'
