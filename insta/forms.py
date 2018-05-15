from django import forms
from .models import Profile, Image


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageUpload(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post_date', 'image_owner']

class profileEdit(forms.Form):
    name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    website = forms.URLField(initial='http://')
    Bio = forms.Textarea()
    Email = forms.EmailField()
    phone_number = forms.CharField(max_length=12)
    Gender = forms.CharField(max_length=6)
