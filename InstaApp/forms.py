from django import forms

from InstaApp.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        fields = ('photo', 'caption', )
        model = Post

class UpdatePostForm(forms.ModelForm):
    class Meta:
        fields = ('photo', 'caption', )
        model = Post