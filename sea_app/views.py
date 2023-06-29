from rest_framework import generics
from rest_framework.response import Response
from .models import Imovel, Anuncio, Reserva
from .serializers import ImovelSerializer, AnuncioSerializer, ReservaSerializer

class ListImovelView(generics.ListCreateAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class DetailImovelView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer

class ListAnuncioView(generics.ListCreateAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

class DetailAnuncioView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer

    def destroy(self, request, *args, **kwargs):
        return Response(status=405)

class ListReservaView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class DetailReservaView(generics.RetrieveDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer