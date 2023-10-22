from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import Post


class CommentForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Leave a comment!",
            }
        ),
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CategoryForm(forms.Form):
    name = forms.CharField(max_length=55)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["categories", "title", "body",]
        