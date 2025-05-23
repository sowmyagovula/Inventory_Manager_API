from django import forms
from .models import Inventory_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory_model
        fields = ['category', 'product_name', 'price', 'stock', 'image']