from django.forms import ModelForm

from exchange_app.category.models import Category



class CategoryCreateForm(ModelForm):

    class Meta:
        model = Category
        fields = ['name']
