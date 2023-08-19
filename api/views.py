from rest_framework import viewsets,status,views,generics,filters
from .models import ColorPalette, FavoritePalettes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .serializers import ColorPaletteSerializer, FavoritePalettesSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ColorPaletteViewSet(viewsets.ModelViewSet):
    '''show all color palette'''
    queryset = ColorPalette.objects.all()
    serializer_class = ColorPaletteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoritePalettesViewSet(viewsets.ModelViewSet):
    queryset = FavoritePalettes.objects.all()
    serializer_class = FavoritePalettesSerializer

    def get_queryset(self):
        return FavoritePalettes.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ColorPaletteSearchListView(generics.ListAPIView):
    '''search color palette by name'''
    queryset = ColorPalette.objects.all()
    serializer_class = ColorPaletteSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']


class UpdatePalette(generics.RetrieveUpdateAPIView):
    '''update color palette'''
    queryset = ColorPalette.objects.all()
    serializer_class = ColorPaletteSerializer



class UserLoginView(views.APIView):  
    '''login view'''
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
