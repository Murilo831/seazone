from django.db import models

class Imovel(models.Model):
    codigo = models.CharField(max_length=255, unique=True)
    limite_hospedes = models.IntegerField()
    quantidade_banheiros = models.IntegerField()
    aceita_animais = models.BooleanField()
    valor_limpeza = models.DecimalField(max_digits=8, decimal_places=2)
    data_ativacao = models.DateField(auto_now_add=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

class Anuncio(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    plataforma = models.CharField(max_length=255)
    taxa_plataforma = models.DecimalField(max_digits=8, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

class Reserva(models.Model):
    codigo_reserva = models.CharField(max_length=255, unique=True)
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE)
    data_checkin = models.DateField()
    data_checkout = models.DateField()
    preco_total = models.DecimalField(max_digits=8, decimal_places=2)
    comentario = models.TextField(blank=True)
    numero_hospedes = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
