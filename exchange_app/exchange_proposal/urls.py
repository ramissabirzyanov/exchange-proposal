from django.urls import path
from exchange_app.exchange_proposal import views


urlpatterns = [
    path('', views.EP_ListView.as_view(), name='ep_list'),
    path('create/', views.EP_CreateView.as_view(), name='ep_create'),
    # path('<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),  
]