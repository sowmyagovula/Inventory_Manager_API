from django.shortcuts import render
from .models import Inventory_model
from .forms import UserRegistrationForm, InventoryForm
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


@login_required
def inventory_manage(request):
    user_products = Inventory_model.objects.filter(user=request.user)
    return render(request, 'inventory_manage.html', {'user_products': user_products})


@login_required
def account_details(request):
    return render(request, 'account_details.html')


@login_required
def create_product(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('inventory_manage')
    else:
        form = InventoryForm()
    return render(request, 'create_product.html', {'form': form})


@login_required
def product_edit(request, product_id):
    product = get_object_or_404(Inventory_model, pk=product_id, user = request.user)

    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit = False)
            product.user = request.user
            product.save()
            return redirect('inventory_manage')
    else:
        form = InventoryForm(instance=product)
    return render(request, 'create_product.html', {'form':form})

@login_required
def product_del(request, product_id):
    product = get_object_or_404(Inventory_model, pk = product_id, user = request.user)
    if request.method == 'POST':
        product.delete()
        return redirect('inventory_manage')
    return render(request, 'product_del.html', {'product':product})

