from django import forms
from posts.models import Post
from posts.models import Category


class PostCreateForm(forms.Form):

    title = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )
    content = forms.CharField(
        max_length=500,
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Content'})
    )
    image = forms.ImageField(
        required=False,
    )


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

class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        widget = forms.TextInput(attrs={'placeholder':'Search'})
    )
    category = forms.ModelChoiceField(queryset= Category.objects.all(), required=False, widget = forms.Select())
    orderings = (
        ("created_at", "created_at"),
        ("-created_at", "in descending created_at"),
        ("updated_at", "updated_at"),
        ("-updated_at", "in descending updated_at"),
        ("rate" , "rate"),
        ("-rate" , "in descending rate"),
    )
    ordering = forms.ChoiceField(choices=orderings, required=False, widget=forms.Select())

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','title', 'content']


    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if (title and content) and title.lower() == content.lower():
            raise forms.ValidationError('Title or description must be different')
        return cleaned_data