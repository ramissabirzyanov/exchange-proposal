from django.forms import ModelForm

from exchange_app.ad.models import Ad



class AdCreateForm(ModelForm):

    class Meta:
        model = Ad
        fields = ['title', 'description', 'category', 'image_url', 'condition']


class AdUpdateForm(AdCreateForm):
    pass