from django.shortcuts import render, redirect
from django.contrib import messages
from faperta.models import Dosen, Tendik, Mahasiswa
from faperta.forms import FormDosen
from faperta.forms import FormTendik
from faperta.forms import FormMahasiswa

# Create your views here.
def indexfaperta(request):
    return render(request, 'faperta-muka.html')

def hapus_Dosen(request, id_Dosen):
    Dosen = Dosen.objects.filter(id=id_Dosen)
    Dosen.delete()

    messages.success(request, "Data berhasil dihapus")

    return redirect('Dosen')

def ubah_Dosen(request, id_Dosen):
    dosen = Dosen.objects.get(id=id_Dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui")
            return redirect('ubah_Dosen', id_Dosen=id_Dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }    

    return render(request, template, konteks)
 

def index(request):
    books = Dosen.objects.all()
    stafs = Tendik.objects.all()
    students = Mahasiswa.objects.all()

    konteks = {
        'books': books,
        'stafs': stafs,
        'students': students,
    }
    return render(request, 'dosen.html', konteks)

def tambah_Dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)
    else:
        form = FormDosen()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-dosen.html', konteks)

def tambah_Tendik(request):
    if request.POST:
        form = FormTendik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTendik()
            pesan = "Data berhasil disimpan"
            
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-tendik.html', konteks)
    else:
        form = FormTendik()


    konteks = {
        'form':form,
    }
    return render(request, 'tambah-tendik.html', konteks)
    
def tambah_Mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data berhasil disimpan"
            
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-mahasiswa.html', konteks)
    else:
        form = FormMahasiswa()

    konteks = {
        'form':form,
    }

    return render(request, 'tambah-mahasiswa.html', konteks)