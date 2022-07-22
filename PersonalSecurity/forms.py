from django import forms
from BusinessSecurity import models


class AddServiceForm(forms.ModelForm):
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-select'}),
                                      queryset=models.ServiceCategory.objects.filter(category_choice='pcs'))

    # assign_to = forms.ModelChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-select js-example-basic-multiple'}), queryset=models.User.objects.filter(is_sales=True))

    # service_icon = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Service
        fields = ['category', 'service_icon', 'service_title', 'short_description', 'service_header', 'service_body', 'service_footer', ]


class AddSubscriptionServiceForm(forms.ModelForm):
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-select'}),
                                      queryset=models.ServiceCategory.objects.filter(category_choice='pcs'))

    # assign_to = forms.ModelChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-select js-example-basic-multiple'}), queryset=models.User.objects.filter(is_sales=True))

    # service_icon = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.SubscriptionServices
        fields = ['category', 'service_icon', 'service_title', 'short_description', 'service_header', 'service_body',
                  'service_footer', ]


class AddPackageForm(forms.ModelForm):
    service_id = forms.ModelChoiceField(
        queryset=models.SubscriptionServices.objects.filter(category_choice='pcs'))

    class Meta:
        model = models.SubscriptionBasedPackage
        fields = '__all__'
        exclude = ['package_id', 'category_choice', 'max_user']


class AddSubServiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=models.Service.objects.filter(has_sub_service=True, category_choice='pcs'),
        widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = models.SubService
        fields = '__all__'
        exclude = ['total_customer', ]
        widgets = {
            'fields': forms.SelectMultiple(attrs={'class': 'form-select js-example-basic-multiple'})
        }
