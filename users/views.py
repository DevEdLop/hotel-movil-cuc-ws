from rest_framework import viewsets
from .api.serializer import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from rest_framework import status
import hashlib
# Create your views here.


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@api_view(['GET'])
def login(request):
    # print(request.data)
    if request.method == 'GET':
        email = request.data['email']
        password = hashlib.sha256(request.data['password'].encode('utf-8')).hexdigest()
        usuario = User.objects.filter(email=email, password=password)
        print('RRRR')
        print(usuario.exists())
        if not usuario.exists():
            return Response({'mensaje': 'No se encuentra el usuario'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'mensaje': 'Inicio exitoso'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    user_serializer = UserSerializer(data=request.data)
    hashed_password = hashlib.sha256(request.data['password'].encode('utf-8')).hexdigest()
    request.data['password'] = hashed_password
    print(request.data['password'])
    if user_serializer.is_valid(raise_exception=True):
        user_serializer.save()
        return Response({'mensaje': 'Usuario creado exitosamente'}, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


