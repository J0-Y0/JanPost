from django import forms
from .models import Comment
from mptt.forms import TreeNodeChoiceField

class CommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(
        queryset=Comment.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control d-none'}),
        required=False
    )  
    class Meta:
        model = Comment
        fields = ('name','parent', 'email', 'content')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
class PostSearchForm(forms.Form):
    searchField = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-secondary','placeholder':'Search'}  ),required=False)
           