import requests
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser

def HomePageView(request):

    users = CustomUser.objects.all().exclude(id=1).order_by('-first_name').order_by('-last_name')

    return render(request, 'accounts/home.html', {'users':users})

def SignupView(request):
    names = requests.get('http://gerador-nomes.herokuapp.com/nome/aleatorio').json()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username = '---',
                first_name = names[0],
                last_name = names[1],
                idade = cd.get('idade'),
                email = cd.get('email'),
                nascimento = cd.get('nascimento'),
                apelido = cd.get('apelido'),
                observação = cd.get('observação'),
            )
        return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form':form})
