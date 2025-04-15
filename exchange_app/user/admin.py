from django.contrib import admin


from django.contrib import admin
from .models import User


@admin.register(User)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
