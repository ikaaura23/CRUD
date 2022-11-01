from django.shortcuts import render
from fkip.forms import FormDosen
from fkip.forms import FormTendik
from fkip.forms import FormMahasiswa

# Create your views here.
def indexfkip(request):
    return render(request, 'fkip-muka.html')

def dosenfkip(request):
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
            return render(request, 'dosenfkip.html', konteks)
    else:
        form = FormDosen()

    konteks = {
        'form': form,
    }

    return render(request, 'dosenfkip.html', konteks)

def tendikfkip(request):
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
            return render(request, 'tendikfkip.html', konteks)
    else:
        form = FormTendik()


    konteks = {
        'form':form,
    }
    return render(request, 'tendikfkip.html', konteks)
    
def mahasiswafkip(request):
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
            return render(request, 'mahasiswafkip.html', konteks)
    else:
        form = FormMahasiswa()

    konteks = {
        'form':form,
    }

    return render(request, 'mahasiswafkip.html', konteks)
    