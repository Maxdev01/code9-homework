from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout 
from account.forms import UserForm 
from portfolio.models import Profile


def deconnecter(request):
    logout(request)
    return redirect('first')

def inscription(request):
    if request.method == "POST":
        myform = UserForm(data=request.POST)
        if myform.is_valid():
            data = myform.cleaned_data
            my_user = myform.save(commit=False)
            my_user.set_password(data.get('password'))
            my_user.save()
            profil_auto = Profile(user=my_user, name="notyet", last_name="notyet", email="code1234@gamil.com")
            profil_auto.save()
            return redirect('first')
    else:
        myform = UserForm()
    context = {'myform': myform}
    return render(request, 'signup.html', context)

def connexion(request):
    if request.method == 'POST':
        data = request.POST
        myform = authenticate(request, username=data['username'], password=data['password'])
        if myform is not None:
            login(request, myform)
            return redirect('dash')
        else:
            print('Pas de compte')
            myform = UserForm()
            context = {"myform": myform}
            return render(request, 'login.html', context)
    else:
        myform = UserForm()
    context = {'myform': myform}
    return render(request, 'login.html', context=context)
