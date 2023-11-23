from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter() 
router.register( r'', views.RoomView,'rooms')


urlpatterns = [
    path('', include(router.urls)),
    path('create_room', view=views.create_room),
    path('update_room/<room_id>', view=views.update_room),
    path('delete_room/<room_id>', view=views.delete_room)
]
