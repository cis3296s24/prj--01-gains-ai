from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Prompt
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import CreateUserForm, LoginForm

def index(request):
    return render(request, 'index.html', {})

def form(request):
    return render(request, 'form.html', {})

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            messages.success(request, (form.errors))
            return render(request, 'signup.html', {})
        messages.success(request, ('Signed Up Successfully'))
        return redirect('homepage')
    else:
        return render(request, 'signup.html', {})
    
def login_user(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        print(form)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request = request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, ('You have been Logged In'))
                user = request.user
                username = user.username
                email = user.email
                first_name = user.first_name
                last_name = user.last_name
                context = {
                    'username': username,
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                }
                return render(request, 'homepage.html', context=context)
        else:
            messages.success(request, ('Incorrect Username or Password'))
            return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been Logged Out'))
    return redirect('homepage')

def about(request):
    return render(request, 'About.html', {})


def workout(request):
    return render(request, 'Workout.html', {})

def music(request):
    return render(request, 'Music.html', {})

def community(request):
    return render(request, 'Community.html', {})

def checkin(request):
    return render(request, 'Checkin.html', {})

def diet(request):
    return render(request, 'Diet.html', {})

def dietform(request):
    return render(request, 'DietForm.html', {})

@login_required
def save_sentence(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            age = request.POST.get('age', '')
            gender = request.POST.get('gender', '')
            duration = request.POST.get('duration', '')
            fitness = request.POST.get('fitness', '')
            typeofworkout = request.POST.get('typeofworkout', '')
            other = request.POST.get('other', '')
            # Construct the sentence
            if typeofworkout == "other":
                sentence = f"`Give me 5 {other} exercises at the gym for {gender} age {age} with a description that last for {duration} minutes for {fitness} seperated by :`;"
            else:
                sentence = f"`Give me 5 {typeofworkout} exercises at the gym for {gender} age {age} with a description that last for {duration} minutes for {fitness} seperated by :`;"
            # Save the sentence to the database
            Prompt_instance = Prompt(sentence=sentence, user=request.user)
            Prompt_instance.save()
            return redirect('workout')  # Redirect to success page
        else:
            return redirect('workout')
    messages.error(request, "Error has occured")
    return render(request, 'index')  # Render the form template

def history(request):
    pass

def success(request):
    return render(request, 'success.html', {})
    
    
