from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

from django.forms import ModelChoiceField
from django.contrib.auth import get_user_model, models
from django.contrib.auth import forms as admin_forms

class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    group = ModelChoiceField(
        queryset=models.Group.objects.all(),
        required=True,
        label=("Grupo de permissões"),
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Informe um endereço de e-mail válido.')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'cargo','name','email','group')
        widgets = {
            'cargo': forms.Select(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),

            # 'group' :forms.Select(attrs={
            #     "class": "form-control",
            #     "style": "height:45px; border:none; border-radius:10px"
            # }),
        }
 

    name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    group = ModelChoiceField(
        queryset=models.Group.objects.all(),
        required=True,
        label=("Grupo de permissões"),
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }
        ),
    )


    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_superuser = False
    #     user.email = self.cleaned_data['email']
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user

    
    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])

       
        if commit:
            user.save()
        user.groups.remove(*user.groups.all())
        user.groups.add(self.cleaned_data["group"])
        return user