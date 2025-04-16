from django.contrib import admin
from django.urls import path, include

from exchange_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('users/', include('exchange_app.user.urls'), name='users'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]  
