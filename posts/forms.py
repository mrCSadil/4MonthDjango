from django import forms
from posts.models import Post

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image','title', 'content']


    # image = forms.ImageField(required=False)
    # title = forms.CharField(required=False , max_length=100)
    # content = forms.CharField(required=False, max_length=400)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('content')
        if (title and description) and title.lower() == description.lower():
            raise forms.ValidationError('Title or description must be different')
        return cleaned_data