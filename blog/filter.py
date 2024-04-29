import django_filters
from .models import Post,Category
from django.forms.widgets import TextInput,DateInput,ChoiceWidget,NumberInput,Select


class PostFilterForm(django_filters.FilterSet):
    title  = django_filters.CharFilter(lookup_expr="icontains",widget=TextInput(attrs={'placeholder': 'Title key word','class':"form-control my-2"}))

    content = django_filters.CharFilter(lookup_expr="icontains",widget=TextInput(attrs={'placeholder': 'some key word','class':"form-control "}))
    published_date = django_filters.DateFilter(lookup_expr='gt',widget=DateInput(attrs={'placeholder': 'published date',"pattern":"\d{2}-\m{2}-\y{4}", "format" :'dd-mm-yyyy' , 'type':'date','class':"form-control my-2"}))
    category = django_filters.ModelChoiceFilter(queryset = Category.objects.all(), widget=Select(attrs={'class':"  my-2  form-select"}))
    class Meta:
        model = Post
        fields = ["title","content","category","published_date",]
        
        
     