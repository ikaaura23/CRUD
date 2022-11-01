from django.shortcuts import render, redirect
from django.contrib import messages
from faperta.models import Dosen, Tendik, Mahasiswa
from fh.forms import FormDosen
from fh.forms import FormTendik
from fh.forms import FormMahasiswa

# Create your views here.
def indexfh(request):
    return render(request, 'fh-muka.html')

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

def dosenfh(request):
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
            return render(request, 'dosenfh.html', konteks)
    else:
        form = FormDosen()

    konteks = {
        'form': form,
    }

    return render(request, 'dosenfh.html', konteks)

def tendikfh(request):
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
            return render(request, 'tendikfh.html', konteks)
    else:
        form = FormTendik()


    konteks = {
        'form':form,
    }
    return render(request, 'tendikfh.html', konteks)
    
def mahasiswafh(request):
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
            return render(request, 'mahasiswafh.html', konteks)
    else:
        form = FormMahasiswa()

    konteks = {
        'form':form,
    }

    return render(request, 'mahasiswafh.html', konteks)