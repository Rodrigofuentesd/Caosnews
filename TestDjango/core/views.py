from django.shortcuts import redirect, render
from .models import Registro
from .forms import RegistroForm

# Create your views here.

def home(request):
        return render(request, 'core/index-invitado.html')

def home_usuario(request):
        return render(request, 'core/index-usuario.html')

def home_editor_user(request):
        return render(request, 'core/index-editor-user.html')

def home_editor_editor(request):
        return render(request, 'core/index-editor-editor.html')

def create_user(request):
        return render(request, 'core/create-user.html')

def new_1(request):
        return render(request, 'core/new-1.html')

def new_1_editor(request):
        return render(request, 'core/new-1-editor.html')

def new_template(request):
        return render(request, 'core/new-template.html')

def create_user(request):
        datos = {
                'form': RegistroForm()
        }
        if request.method=='POST':
                formulario = RegistroForm(request.POST)
                if formulario.is_valid:
                        formulario.save()
                        datos['mensaje'] = "Guardados correctamente"

        return render(request,'core/create-user.html',datos)