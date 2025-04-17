from django.urls import path
from exchange_app.category import views


urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('create/', views.CategoryCreateView.as_view(), name='categiry_create'),
]