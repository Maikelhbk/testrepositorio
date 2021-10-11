from django.shortcuts import redirect, render, get_object_or_404
from .models import Cliente, Profesional
from .form import ClienteForm, ProfesionalForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.



def home(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes': clientes
    }
    return render(request, 'app/home.html', data)

def cliente(request):
    data = {
        'form': ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Cliente creado correctamente"
        else:
            data["form"] = formulario
            data["mensaje"] = "Error al crear al usuario"
    return render(request, 'app/cliente.html', data)

def profesional(request):
    data = {
        'form_pro': ProfesionalForm
    }
    if request.method == 'POST':
        formulario = ProfesionalForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Profesional creado correctamente"
        else:
            data["form"] = formulario
    return render (request, 'app/profesional.html', data)

def registro (request):
    data = {
        'form': CustomUserCreationForm
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registro.html',data)


def menu_cliente(request):
    return render(request, 'app/menu_cliente.html')

def menu_profesional(request):
    return render(request, 'app/menu_profecional.html')


def modificar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    data = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='login')
        data['form'] = formulario

    return render(request, 'app/modificar.html', data)

#def eliminar_producto(request,id):
 #   cliente = get_object_or_404(C)