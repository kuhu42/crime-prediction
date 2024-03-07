# loginanalysis/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
def user_login(request):
if request.method == 'POST':
username = request.POST['username']
password = request.POST['password']
user = authenticate(request, username=username, password=password)
if user is not None:
login(request, user)
return redirect('home')
else:
return render(request, 'loginanalysis/login.html', {'error': 'Invalid
login credentials'})
return render(request, 'loginanalysis/login.html')
def home(request):
return render(request, 'loginanalysis/home.html')
