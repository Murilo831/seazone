# Seazone Code Challenge - APIs Back End

## Tecnologias Utilizadas
<table>
  <tr>
    <td>Python</td>
    <td>Django</td>
    <td>Django Rest Framework</td>
    <td>Banco de dados SQL (Postgre)</td>
  </tr>
  <tr>
    <td>3.10.6</td>
    <td>4.2.2</td>
    <td>3.14.0</td>
    <td>2.9.6</td>
  </tr>
</table>
  
## Configuração do Ambiente
Clone o repositório:

git clone https://github.com/Murilo831/seazone.git

## Instale as dependências:

pip install -r requirements.txt

## Configure o banco de dados:

Crie um banco de dados SQL e atualize as configurações de conexão em settings.py.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
        
    }
}
```
Execute as migrações para criar as tabelas do banco de dados:

+ python manage.py migrate

## Carregue os dados iniciais:

+ python manage.py loaddata imoveis.json
+ python manage.py loaddata anuncios.json
+ python manage.py loaddata reservas.json
  
## APIs
### API 1 - Imóveis
+ GET /api/imoveis/: Retorna uma lista de imóveis.
+ GET /api/imoveis/{id}/: Retorna os detalhes de um imóvel específico.
+ POST /api/imoveis/: Cria um novo imóvel.
+ PUT /api/imoveis/{id}/: Atualiza um imóvel existente.
+ DELETE /api/imoveis/{id}/: Deleta um imóvel existente.
  
### API 2 - Anúncios
+ GET /api/anuncios/: Retorna uma lista de anúncios.
+ GET /api/anuncios/{id}/: Retorna os detalhes de um anúncio específico.
+ POST /api/anuncios/: Cria um novo anúncio.
+ PUT /api/anuncios/{id}/: Atualiza um anúncio existente.
  
### API 3 - Reservas
+ GET /api/reservas/: Retorna uma lista de reservas.
+ GET /api/reservas/{id}/: Retorna os detalhes de uma reserva específica.
+ POST /api/reservas/: Cria uma nova reserva.
+ DELETE /api/reservas/{id}/: Deleta uma reserva existente.
  
## Busca Individual

<p> Para fazer uma busca individual, adicione o parâmetro {id} na URL correspondente à entidade que deseja buscar. Por exemplo:</p>

+ /api/imoveis/1/ - Retorna os detalhes do imóvel com ID 1.
+ /api/anuncios/3/ - Retorna os detalhes do anúncio com ID 3.
+ /api/reservas/2/ - Retorna os detalhes da reserva com ID 2.

## Testes

O projeto inclui um arquivo `tests.py` que contém testes unitários para garantir o correto funcionamento da API. Os testes foram implementados usando a biblioteca de testes do Django e abrangem os principais casos de uso e funcionalidades do sistema.

Esses testes são executados para verificar se as diferentes partes da aplicação estão funcionando conforme o esperado e ajudam a garantir que as alterações no código não quebrem funcionalidades existentes.

Para executar os testes, você pode usar o comando `python manage.py test` no diretório raiz do projeto. Isso garantirá que a aplicação esteja em conformidade com os requisitos definidos e evitará regressões indesejadas.
