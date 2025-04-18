from django.contrib import admin


from django.contrib import admin
from .models import ExchangeProposal


@admin.register(ExchangeProposal)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'ad', 'sender', 'reciever', 'status')
