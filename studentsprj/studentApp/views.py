from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "index.html")

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')  # Change 'pass1' to 'password'
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('studentlist')
        else:
            messages.error(request, 'Wrong credentials!')
    
    return render(request, "sign_in.html")

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')  # Change 'pass1' to 'password'
        password2 = request.POST.get('password2')  # Change 'pass2' to 'password2'
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('index')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('index')
        
        if password != password2:
            messages.error(request, "Passwords didn't match")
        else:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            messages.success(request, "Your account has been successfully created.")
            return redirect('sign_in')
    else:
        messages.error(request, "Passwords do not match.")
    return render(request, "sign_up.html")

def sign_out(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('index')

# @login_required
def studentlist(request):
    students = Student.objects.all()  # Fetch all student objects from the database
    return render(request, 'studentlist.html', {'students': students})

# @login_required
def studentform(request, id=0):

    if request.method == "POST":
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = get_object_or_404(Student, pk=id)
            form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('studentlist')
    else:
        if id == 0:
            form = StudentForm()
        else:
            student = get_object_or_404(Student, pk=id)
            form = StudentForm(instance=student)

    return render(request, "studentform.html", {'form': form})

def studentdelete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('studentlist')
