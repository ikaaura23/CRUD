from tkinter import Widget
from django.forms import ModelForm
from django import forms 
from faperta.models import Dosen, Tendik, Mahasiswa

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        fields = '__all__'

    widgets = {
        'NIP' : forms.TextInput({'class':'form-control'}),
        'Nama' : forms.TextInput({'class':'form-control'}),
        'TanggalLahir' : forms.TextInput({'class':'form-control'}),
        'Email' : forms.TextInput({'class':'form-control'}),
        'Photo' : forms.TextInput({'class':'form-control'}),
        'Fakultas' : forms.TextInput({'class':'form-control'}),
        'Prodi' : forms.TextInput({'class':'form-control'}),
        'Alamatrumah' : forms.TextInput({'class':'form-control'}),
     }

class FormTendik(ModelForm):
    class Meta:
        model = Tendik
        fields = '__all__'
widgets = {
        'NIP' : forms.TextInput({'class':'form-control'}),
        'Nama' : forms.TextInput({'class':'form-control'}),
        'TanggalLahir' : forms.TextInput({'class':'form-control'}),
        'Photo' : forms.TextInput({'class':'form-control'}),
        'Email' : forms.TextInput({'class':'form-control'}),
        'Unit' : forms.TextInput({'class':'form-control'}),
        'Alamatrumah' : forms.TextInput({'class':'form-control'}),
     }
   
class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'
    
    widgets = {
        'NIM' : forms.TextInput({'class':'form-control'}),
        'Nama' : forms.TextInput({'class':'form-control'}),
        'TanggalLahir' : forms.TextInput({'class':'form-control'}),
        'Email' : forms.TextInput({'class':'form-control'}),
        'Photo' : forms.TextInput({'class':'form-control'}),
        'Fakultas' : forms.TextInput({'class':'form-control'}),
        'Prodi' : forms.TextInput({'class':'form-control'}),
     }