from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from users.forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginUser(request):
    page = 'login'
    context = {"page": page, }

    # for restricting login user to go to login page again
    if request.user.is_authenticated:
        return (redirect('users:profiles'))

    # for submitted login form
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is not correct.")

    # for a user to present empty login form
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('users:login')


def registerUser(request):
    # for restricting login user to go to register page again
    if request.user.is_authenticated:
        return (redirect('users:profiles'))

    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User account was created!")
            login(request, user)
            return redirect('users:edit-account')
        else:
            messages.error(request, "An error has occured! Try again!")

    context = {"page": page, "form": form}
    return render(request, 'users/login_register.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    return render(request, 'users/profiles.html', {"profiles": profiles})


def profile_detail(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description__exact="")
    context = {
        "profile": profile,
        "topSkills": topSkills,
        "otherSkills": otherSkills,
    }
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='users:login')
def userAccount(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request, 'users/account.html', context)


@login_required(login_url='users:login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("users:account")

    context = {"profile": profile, "form": form}
    return render(request, 'users/profile-form.html', context)
