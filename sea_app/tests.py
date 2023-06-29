from django.test import TestCase
from rest_framework.test import APIClient
from .models import Imovel, Anuncio, Reserva

class ImovelAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.imovel_data = {
            'codigo': 'IM001',
            'limite_hospedes': 4,
            'quantidade_banheiros': 2,
            'aceita_animais': True,
            'valor_limpeza': '50.00',
        }
        self.imovel = Imovel.objects.create(**self.imovel_data)

    def test_get_imovel_list(self):
        response = self.client.get('/api/imoveis/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['codigo'], self.imovel_data['codigo'])

    
    def test_get_imovel_detail(self):
        response = self.client.get(f'/api/imoveis/{self.imovel.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['codigo'], self.imovel_data['codigo'])

    def test_create_imovel(self):
        new_imovel_data = {
            'codigo': 'IM002',
            'limite_hospedes': 6,
            'quantidade_banheiros': 3,
            'aceita_animais': False,
            'valor_limpeza': '75.00',
        }
        response = self.client.post('/api/imoveis/', data=new_imovel_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Imovel.objects.count(), 2)

    def test_update_imovel(self):
        updated_imovel_data = {
            'codigo': 'IM002',
            'limite_hospedes': 5,
            'quantidade_banheiros': 3,
            'aceita_animais': False,
            'valor_limpeza': '60.00',
        }

        response = self.client.put(f'/api/imoveis/{self.imovel.pk}/', data=updated_imovel_data, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.imovel.refresh_from_db()
        self.assertEqual(self.imovel.limite_hospedes, updated_imovel_data['limite_hospedes'])

    def test_delete_imovel(self):
        response = self.client.delete(f'/api/imoveis/{self.imovel.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Imovel.objects.count(), 0)

class AnuncioAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.imovel = Imovel.objects.create(
            codigo='IM001',
            limite_hospedes=4,
            quantidade_banheiros=2,
            aceita_animais=True,
            valor_limpeza='50.00'
        )
        self.anuncio_data = {
            'imovel': self.imovel,
            'plataforma': 'Airbnb',
            'taxa_plataforma': '10.00',
        }
        self.anuncio = Anuncio.objects.create(**self.anuncio_data)

    def test_get_anuncio_list(self):
        response = self.client.get('/api/anuncios/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['plataforma'], self.anuncio_data['plataforma'])

    def test_get_anuncio_detail(self):
        response = self.client.get(f'/api/anuncios/{self.anuncio.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['plataforma'], self.anuncio_data['plataforma'])

    def test_create_anuncio(self):
        new_anuncio_data = {
            'imovel': self.imovel.pk,
            'plataforma': 'Booking',
            'taxa_plataforma': '15.00',
        }
        response = self.client.post('/api/anuncios/', data=new_anuncio_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Anuncio.objects.count(), 2)

    def test_update_anuncio(self):
        updated_anuncio_data = {
            'imovel': self.imovel.pk,
            'plataforma': 'Vrbo',
            'taxa_plataforma': '12.00',
        }
        response = self.client.put(f'/api/anuncios/{self.anuncio.pk}/', data=updated_anuncio_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.anuncio.refresh_from_db()
        self.assertEqual(self.anuncio.plataforma, updated_anuncio_data['plataforma'])
    
    def test_delete_anuncio(self):
        response = self.client.delete(f'/api/anuncios/{self.anuncio.pk}/')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(Anuncio.objects.count(), 1)

class ReservaAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.imovel = Imovel.objects.create(
            codigo='IM001',
            limite_hospedes=4,
            quantidade_banheiros=2,
            aceita_animais=True,
            valor_limpeza='50.00',
        )
        self.anuncio = Anuncio.objects.create(
            imovel=self.imovel,
            plataforma='Airbnb',
            taxa_plataforma='10.00',
        )
        self.reserva_data = {
            'codigo_reserva': 'R001',
            'anuncio': self.anuncio,
            'data_checkin': '2022-01-01',
            'data_checkout': '2022-01-10',
            'preco_total': '500.00',
            'comentario': 'Ótima estadia!',
            'numero_hospedes': 2,
        }
        self.reserva = Reserva.objects.create(**self.reserva_data)

    def test_get_reserva_list(self):
        response = self.client.get('/api/reservas/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['codigo_reserva'], self.reserva_data['codigo_reserva'])
    
    def test_get_reserva_detail(self):
        response = self.client.get(f'/api/reservas/{self.reserva.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['codigo_reserva'], self.reserva_data['codigo_reserva'])

    def test_create_reserva(self):
        new_reserva_data = {
            'codigo_reserva': 'R002',
            'anuncio': self.anuncio.pk,
            'data_checkin': '2022-02-01',
            'data_checkout': '2022-02-10',
            'preco_total': '600.00',
            'comentario': 'Excelente hospedagem!',
            'numero_hospedes': 3,
        }
        response = self.client.post('/api/reservas/', data=new_reserva_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Reserva.objects.count(), 2)

    def test_update_reserva(self):
        updated_reserva_data = {
            'codigo_reserva': 'R002',
            'anuncio': self.anuncio.pk,
            'data_checkin': '2022-03-01',
            'data_checkout': '2022-03-10',
            'preco_total': '700.00',
            'comentario': 'Muito bom!',
            'numero_hospedes': 4,
        }
        response = self.client.put(f'/api/reservas/{self.reserva.pk}/', data=updated_reserva_data, format='json')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(Reserva.objects.get(pk=self.reserva.pk).codigo_reserva, self.reserva.codigo_reserva)
    
    def test_delete_reserva(self):
        response = self.client.delete(f'/api/reservas/{self.reserva.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Reserva.objects.count(), 0)