from django import forms
from django.forms import widgets
from Blog import models


class PostForm(forms.ModelForm):
    # feature_image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    comment_option = forms.ChoiceField(choices=models.COMMENT_OPTIONS,
                                       widget=forms.Select(attrs={'class': 'form-select'}))

    # post_url = forms.CharField(widget=forms.TextInput(
    #     attrs={'pattern': '([a-zA-Z0-9]|[-]|[_])'}))

    class Meta:
        model = models.Post
        fields = ['post_url', 'title', 'feature_image', 'short_description', 'content',
                  'comment_option', ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.BlogCategory
        fields = '__all__'


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = models.BlogSubCategory
        fields = '__all__'


class FilterOptionForm(forms.ModelForm):
    class Meta:
        model = models.FilterOption
        fields = '__all__'


# class BlogSubscriptionForm(forms.ModelForm):
#     class Meta:
#         model = models.BlogSubscription
#         fields = '__all__'
#         widgets = {
#             'full_name': forms.TextInput(attrs={'placeholder': 'Enter Your Name'}),
#             'email': forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}),
#         }
