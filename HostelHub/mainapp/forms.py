# from django import forms
# from .models import HostelAd


# class HostelAdForm(forms.ModelForm):
#     class Meta:
#         model = HostelAd
#         fields = ["title", "description", "city", "area", "hostel_type"]


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser, HostelAd


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "phoneno",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phoneno = self.cleaned_data["phoneno"]
        if commit:
            user.save()
        return user


class HostelAdForm(forms.ModelForm):
    class Meta:
        model = HostelAd
        fields = ["title", "description", "city", "area", "price", "image"]
