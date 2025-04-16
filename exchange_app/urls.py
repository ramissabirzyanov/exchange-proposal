from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from exchange_app.user.views import UsersAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from exchange_app import views


router = DefaultRouter()
router.register(r'api/users', UsersAPIView)

schema_view = get_schema_view(
    openapi.Info(title="API Documentation", default_version="v1"),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-doc"),
    path('', views.IndexView.as_view(), name='index'),
    path('users/', include('exchange_app.user.urls'), name='users'),
    path('ads/', include('exchange_app.ad.urls'), name='ad_list'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]  

urlpatterns += [
    path('', include(router.urls))
]
