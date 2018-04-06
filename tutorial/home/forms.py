from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(max_length=500)

    class Meta:
        model = Post
        fields = ('post',)