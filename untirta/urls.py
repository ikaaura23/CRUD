from django.contrib import admin
from django.urls import path
from fkip.views import indexfkip
from faperta.views import indexfaperta
from feb.views import indexfeb
from fh.views import indexfh
from fisip.views import indexfisip
from fk.views import indexfk
from ft.views import indexft
from pascasarjana.views import indexpascasarjana
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fkip/', indexfkip),
    path('faperta/', indexfaperta),
    path('feb/', indexfeb),
    path('fh/', indexfh),
    path('fisip/', indexfisip),
    path('fk/', indexfk),
    path('ft/', indexft),
    path('pascasarjana/', indexpascasarjana),
]
