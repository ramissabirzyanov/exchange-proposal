from django.urls import path
from exchange_app.user import views


urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]