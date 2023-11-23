from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register( r'', views.BookingView,'rooms')


urlpatterns = [
    path('', include(router.urls)),
    path('create_booking', view=views.create_booking),
    path('update_booking/<booking_id>', view=views.update_booking),
    path('delete_booking/<booking_id>', view=views.delete_booking)
]
