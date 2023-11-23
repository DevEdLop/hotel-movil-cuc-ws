from rest_framework import viewsets
from .api.serializer import BookingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking
from rest_framework import status

class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()



@api_view(['POST'])
def create_booking(request):
    booking_serializer = BookingSerializer(data=request.data)
    if booking_serializer.is_valid():
        booking_serializer.save()
        return Response({'mensaje': 'Reserva creada exitosamente'}, status=status.HTTP_201_CREATED)
    return Response(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_booking(request, booking_id):
    try:
        booking_instance = Booking.objects.get(pk=booking_id)
    except Booking.DoesNotExist:
        return Response({'mensaje': 'La reserva no existe'}, status=status.HTTP_404_NOT_FOUND)

    booking_serializer = BookingSerializer(booking_instance, data=request.data, partial=True)
    if booking_serializer.is_valid():
        booking_serializer.save()
        return Response({'mensaje': 'Reserva editada exitosamente'}, status=status.HTTP_200_OK)

    return Response(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_booking(request, booking_id):
    try:
        booking_instance = Booking.objects.get(pk=booking_id)
        booking_instance.delete()
        return Response({'mensaje': 'Reserva eliminada exitosamente'}, status=status.HTTP_204_NO_CONTENT)
    except Booking.DoesNotExist:
        return Response({'mensaje': 'La reserva no existe'}, status=status.HTTP_404_NOT_FOUND)
