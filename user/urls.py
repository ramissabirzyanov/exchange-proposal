from django.urls import path
from exchange_app.user import views


urlpatterns = [
    path('',
         views.UsersListView.as_view(),
         name='users'),
]