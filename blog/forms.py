from django import forms
from .models import Comment,Report










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
# class PostSearchForm(forms.Form):
#     searchField = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-primary-subtle','placeholder':'Search'}  ),required=False)

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('post','name', 'type', 'detail')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.Select(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'rows':'3','placeholder':"Please enter any additional details relevant to your report"}),
        }

