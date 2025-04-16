from django.contrib import admin


from django.contrib import admin
from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
