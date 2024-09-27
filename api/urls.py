from django.urls import include, path
from djoser import views as djoser_views
from rest_framework.routers import DefaultRouter

from api.views import (CartModelViewSet, CategoryModelViewSet,
                       ProductModelViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('categories', CategoryModelViewSet, basename='categories')
router.register('products', ProductModelViewSet, basename='products')
router.register('cart', CartModelViewSet, basename='cart')

# POST /auth/users/register/ - регистрация
# POST /auth/token/login/ - аутентификация
# POST /auth/token/logout/ - логаут
urlpatterns = [
    path('', include(router.urls)),
    path('auth/users/register/', djoser_views.UserViewSet.as_view({'post': 'create'}), name='register'),
    path('auth/token/login/', djoser_views.TokenCreateView.as_view(), name='login'),
    path('auth/token/logout/', djoser_views.TokenDestroyView.as_view(), name='logout'),
    # path("auth/", include('djoser.urls')),
    # path("auth/", include('djoser.urls.authtoken')),
]
