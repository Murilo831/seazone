from django.urls import path
from .views import ListImovelView, DetailImovelView, ListAnuncioView, DetailAnuncioView, ListReservaView, DetailReservaView

urlpatterns = [
    path('imoveis/', ListImovelView.as_view(), name='imovel-list'),
    path('imoveis/<int:pk>/', DetailImovelView.as_view(), name='imovel-detail'),
    path('anuncios/', ListAnuncioView.as_view(), name='anuncio-list'),
    path('anuncios/<int:pk>/', DetailAnuncioView.as_view(), name='anuncio-detail'),
    path('reservas/', ListReservaView.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', DetailReservaView.as_view(), name='reserva-detail'),
]