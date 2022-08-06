#DEV

Django commands

django-admin startproject <nazwa projektu> - tworzy nowy projekt
python manage.py createsuperuser - tworzy admina
python manage.py runserver - uruchamia server
python manage.py migrate / python manage.py makemigrations - migracje
python manage.py startapp <nazwa aplikacji> - tworzy nową aplikację

Python shell django commands

from product.models import Prodcut - importuje mi klasę Prodcut z pliku prodcut/models
Product.objects.all() - wyświetla mi wszystkie objekty tej apliacji (produkty)
Product.objects.create() - tworzy nowy obiekt (produkt)

Product.objects.create(name='nic',description='nic',price='100zł',summary='nic')

docker-compose up - uruchamia polecnia docker
docker ps - wypisuje wszystkie image
docker exec -it <3 pierwsze znaki image> bash - otwiera tryb konsoli danego image
docker-compose build <nazwa pliku> - buduje container