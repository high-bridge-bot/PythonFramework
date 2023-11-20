from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = \
        'user name'
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        
        self.fields['email'].widget.attrs['placeholder'] = \
        'Email adress'
        
        self.fields['email'].widget.attrs['class'] = 'form-control'
        
        self.fields['password1'].widget.attrs['placeholder'] = \
        'Password'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        
        self.fields['password2'].widget.attrs['placeholder'] = \
        'Confirm Password'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'