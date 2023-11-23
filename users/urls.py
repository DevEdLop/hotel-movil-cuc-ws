from django.urls import path, include
from rest_framework import routers
# from django.conf.urls import handler404
from . import views


router = routers.DefaultRouter()
router.register(r'', views.UserView, 'users')


urlpatterns = [
    path('', include(router.urls)),
    path('login', view=views.login),
    path('register', view=views.register),
    # handler404(r'^no-encontrado/$', views.no_encontrado, name='no_encontrado'),
]
