from django.urls import path
from exchange_app.ad import views


urlpatterns = [
    path('', views.AdListView.as_view(), name='ads'),
    path('create/', views.AdCreateView.as_view(), name='ad_create'),
    # path('<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),  
]