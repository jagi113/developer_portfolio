from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.models import Profile, Message
from django.contrib.auth.models import User
from django.contrib import messages
from users.forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from django.contrib.auth.decorators import login_required
from users.utils import searchProfiles, paginateProfiles


# Create your views here.


def loginUser(request):
    page = 'login'
    context = {"page": page, }

    # for restricting login user to go to login page again
    if request.user.is_authenticated:
        return (redirect('users:profiles'))

    # for submitted login form
    if request.method == 'POST':
        username = request.POST['username']. lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'users:account')
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
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request, profiles, 12)

    context = {"profiles": profiles,
               "search_query": search_query,
               "custom_range": custom_range
               }
    return render(request, 'users/profiles.html', context)


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


@login_required(login_url='users:login')
def createSkill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
            return redirect('users:account')

    context = {"form": form, "page": "create"}
    return render(request, 'users/skill-form.html', context)


@login_required(login_url='users:login')
def editSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
            return redirect("users:account")

    context = {"form": form, "page": "edit", "skill": skill}
    return render(request, 'users/skill-form.html', context)


@login_required(login_url='users:login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)

    if request.method == "POST":
        skill.delete()
        return redirect("users:account")
    
@login_required(login_url='users:login')
def inbox(request):
    message_set = Message.objects.filter(recipient=request.user.profile)
    new_messages = message_set.filter(is_read=False).count()
    context = {"messages_set":message_set, "new_messages":new_messages}
    return render(request, 'users/inbox.html', context)

@login_required(login_url='users:login')
def messageDetail(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {"message":message}
    return render(request, 'users/message.html', context)

def createMessage(request, recipient):
    form = MessageForm()
    message = form.save(commit=False)
    message.recipient = Profile.objects.get(pk=recipient)    

    if request.user.is_authenticated:
        message.sender = request.user.profile
        message.email = request.user.profile.email
        message.name = request.user.profile.name
    else: 
        message.sender = None
    form = MessageForm(instance=message)
    
    if request.method == "POST":
        form= MessageForm(request.POST, request.FILES, instance=message)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message was successfully sent!')
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')

    context = {"form": form}
    return render(request, 'users/message-form.html', context)
