from django.contrib import admin
from django.urls import path
from fkip.views import indexfkip, mahasiswafkip, tendikfkip, dosenfkip
from faperta.views import indexfaperta, tambah_Dosen, tambah_Tendik, tambah_Mahasiswa, index
from feb.views import indexfeb, dosenfeb, mahasiswafeb, tendikfeb
from fh.views import indexfh, dosenfh, mahasiswafh, tendikfh
from fisip.views import indexfisip, dosenfisip, mahasiswafisip, tendikfisip
from fk.views import indexfk, dosenfk, mahasiswafk, tendikfk
from ft.views import indexft, dosenft, mahasiswaft, tendikft
from pascasarjana.views import indexpascasarjana, dosenpasca, mahasiswapasca, tendikpasca
from profil.views import indexprofil
from universitas.views import indexuniversitas

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
    path('profil/', indexprofil),
    path('universitas/', indexuniversitas),
    path('tambah-dosen/', tambah_Dosen),
    path('tambah-tendik/', tambah_Tendik),
    path('tambah-mahasiswa/', tambah_Mahasiswa),
    path('dosenfeb/', dosenfeb),
    path('mahasiswafeb/', mahasiswafeb),
    path('tendikfeb/', tendikfeb),
    path('dosenfh/', dosenfh),
    path('tendikfh/', tendikfh),
    path('mahasiswafh/', mahasiswafh),
    path('dosenfisip/', dosenfisip),
    path('tendikfisip/', tendikfisip),
    path('mahasiswafisip/', mahasiswafisip),
    path('dosenfk/', dosenfk),
    path('tendikfk/', tendikfk),
    path('mahasiswafk/', mahasiswafk),
    path('dosenfkip/', dosenfkip),
    path('tendikfkip/', tendikfkip),
    path('mahasiswafkip/', mahasiswafkip),
    path('dosenft/', dosenft),
    path('tendikft/', tendikft),
    path('mahasiswaft/', mahasiswaft),
    path('dosenpasca/', dosenpasca),
    path('tendikpasca/', tendikpasca),
    path('mahasiswapasca/', mahasiswapasca),
    path('dosen/', index),
]

