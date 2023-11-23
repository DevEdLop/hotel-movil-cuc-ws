from rest_framework import viewsets
from .api.serializer import RoomSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rooms.models import Room 
from rest_framework import status


# Create your views here.

class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    

@api_view(['POST'])    
def create_room(request):
    if request.method == 'POST':
        room_serializer = RoomSerializer(data=request.data)
        if room_serializer.is_valid():
           room_serializer.save()
           return Response({'mensaje': 'Habitacion creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def update_room(request, room_id):
    try:
        room_instance = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        return Response({'mensaje': 'La habitación no existe'}, status=status.HTTP_404_NOT_FOUND)

    room_serializer = RoomSerializer(room_instance, data=request.data, partial=True)
    if room_serializer.is_valid():
        room_serializer.save()
        return Response({'mensaje': 'Habitación editada exitosamente'}, status=status.HTTP_200_OK)

    return Response(room_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_room(request, room_id):
    try:
        room_instance = Room.objects.get(pk=room_id)
        room_instance.delete()
        return Response({'mensaje': 'Habitación eliminada exitosamente'}, status=status.HTTP_204_NO_CONTENT)
    except Room.DoesNotExist:
        return Response({'mensaje': 'La habitación no existe'}, status=status.HTTP_404_NOT_FOUND)
