from django.urls import path
from exchange_app.user import views


urlpatterns = [
    path('', views.UsersListView.as_view(), name='users'),
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]