from django.shortcuts import render
from .models import Inventory_model
from .forms import UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.db.models import F, Sum

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('inventory_manage')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def inventory_manage(request):
    return render(request, 'inventory_manage.html')

@login_required
def account_details(request):
    return render(request, 'account_details.html')