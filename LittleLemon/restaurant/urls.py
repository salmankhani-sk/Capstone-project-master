from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('api-token-auth/', obtain_auth_token),
    path('items', views.MenuItemView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view())
]