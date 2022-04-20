from .models import User
from django.contrib.auth.forms import UserCreationForm
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields= [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'address','city', 'zip_code', 'province_number','phone']