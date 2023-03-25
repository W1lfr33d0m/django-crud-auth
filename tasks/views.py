from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
def signup(request):
    
    if request.method == 'GET':
        print('Enviando formulario')
    else:
        if request.POST['password1'] == request.POST['password2']:
            #register User
            try:
                user = User.objects.create_user(username=request.POST['username'], password = request.POST['password1'])
                user.save()
                return HttpResponse('User created successfully')
            except:
                return HttpResponse('Username already exists')
        return HttpResponse('Passwords do not match')
    
    return render(request, 'signup.html', {
        'form': UserCreationForm
    })

def home(request):
    return render(request, 'home.html')