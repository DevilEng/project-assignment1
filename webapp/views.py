from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def hi(request):
    return render(request, "webapp/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')

    return render(request, "webapp/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "webapp/index.html", {'fname': fname})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('Home Page')

    return render(request, "webapp/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "logged Out Successfuly!")
    return redirect('Home Page')
