# Online Menu

###Uruchomienie projektu
Aby uruchomić projekt należy w terminalu wykonać następującą komendę:


`docker-compose up -d --build`

Następnie w app/extra_settings.py, dodać dane autoryzujące do konta email, które będzie wykorzystywane do raportowania.

`EMAIL_HOST_USER = "<adres email>"`

`EMAIL_HOST_PASSWORD = "<hasło do konta>"`


Swagger będzie dostępny pod:

`http://0.0.0.0:8000/api/schema/swagger-ui/`

###Autoryzacja

Autoryzacja opiera się na tokenach JWT.
Logować można się metodą POST pod adresem:

`http://0.0.0.0:8000/api/token/`

`{
    "username": "",
    "password": ""
}`

Token będzie aktywny przez jedną godzine. Token może być odnowiony przez najbliższe 5 dni pod adresem:

`http://0.0.0.0:8000/api/token/refresh/`

`{
    "refresh": ""
}`

###API

Projekt składa się z dwóch głównych elementów jakimi są Menu i Dania(Dish).

`Menu - http://0.0.0.0:8000/api/v1/menu/`

`Dish - http://0.0.0.0:8000/api/v1/dish/`

Oba endpointy po autoryzacji zapewniają wszystkie wszystkie operacje CRUD.
Bez autoryzacji istnieje dostęp tylko do endpointu listowego Menu.
Jednocześnie, bez autoryzacji Menu, zwraca tylko i wyłącznie instancje nie puste (nie zawierające żadnych dań)

###Dane inicjalizacyjne

Do wygenerowania danych można wykorzystać komendę:

`./manage.py generate_data`

Domyślnie wygeneruje 10 Menu i Dań, ilość wygenerowanych instancji możemy kontrolować za pomocą flag 'menus' i 'dishes', przykładowo:

`./manage.py generate_data --menus 3 --dishes -5`

Nazwy Menu utrzymują się w konwencji 'Menu #<iteracja>'. Za pomocą flagi 'unique', zamiast liczby iteracji, zostanie zapisany wygenerowany za pomocą uuid4 string:

`./manage.py generate_data --unique`


