from django import forms
from BusinessSecurity import models
from Academy.models import Course, duration, Section, Content, PackageFeatures, CoursePackage, CoursePurchase
from django.db.models import Q
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils import timezone, dateformat


class AddServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = models.ServiceCategory
        # fields = '__all__'
        exclude = ['category_choice', ]


class AddServiceForm(forms.ModelForm):
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-select'}),
                                      queryset=models.ServiceCategory.objects.filter(category_choice='bcs'))

    # assign_to = forms.ModelChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-select js-example-basic-multiple'}), queryset=models.User.objects.filter(is_sales=True))

    # service_icon = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Service
        fields = ['category', 'service_icon', 'service_title', 'short_description', 'service_header', 'service_body',
                  'service_footer', ]


class AddSubscriptionServiceForm(forms.ModelForm):
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-select'}),
                                      queryset=models.ServiceCategory.objects.filter(category_choice='bcs'))

    # assign_to = forms.ModelChoiceField(widget=forms.SelectMultiple(attrs={'class': 'form-select js-example-basic-multiple'}), queryset=models.User.objects.filter(is_sales=True))

    # service_icon = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.SubscriptionServices
        fields = ['category', 'service_icon', 'service_title', 'short_description', 'service_header', 'service_body',
                  'service_footer', ]


class AddForm(forms.ModelForm):
    class Meta:
        model = models.InputFields
        fields = '__all__'


class AddSubServiceForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=models.Service.objects.filter(has_sub_service=True, category_choice='bcs'),
        widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = models.SubService
        fields = '__all__'
        exclude = ['total_customer', ]
        widgets = {
            'fields': forms.SelectMultiple(attrs={'class': 'form-select js-example-basic-multiple'})
        }


class AddSubscriptionFieldsForm(forms.ModelForm):
    # subscriptionservice = forms.ModelChoiceField(
    #     queryset=models.SubscriptionServices.objects.filter(category_choice='bcs'),
    #     widget=forms.Select(attrs={'class': 'form-select'}), required=False)

    class Meta:
        model = models.SubscriptionField
        fields = '__all__'
        widgets = {
            'fields': forms.SelectMultiple(attrs={'class': 'form-select js-example-basic-multiple'})
        }
        exclude = ['subscriptionservice']


class CreateBusinessForm(forms.ModelForm):
    position = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Designation'}))
    website = forms.URLField(widget=forms.URLInput(
        attrs={'pattern': "^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$",
               'value': "https://"}))

    class Meta:
        model = models.Business
        fields = '__all__'
        exclude = ['unique_id', 'company_logo']

    def clean(self):
 
        # data from the form is fetched using super function
        super(CreateBusinessForm, self).clean()
         
        # extract the email field from the data
        email = self.cleaned_data.get('email')
        email_set={'gmail','protonmail','hotmail','yahoo','zoho','aim','aol','gmx','icloud','yandex'}
        if email.split('@')[1].split('.')[0].lower() in email_set:
              raise forms.ValidationError('The email need to be a bussinees email')

class AddPackageForm(forms.ModelForm):
    service_id = forms.ModelChoiceField(
        queryset=models.SubscriptionServices.objects.filter(category_choice='bcs'))

    class Meta:
        model = models.SubscriptionBasedPackage
        fields = '__all__'
        exclude = ['package_id', 'category_choice']


class AddPackageFeatureForm(forms.ModelForm):
    # service_id = forms.ModelChoiceField(queryset=models.Service.objects.filter(is_subscription_based=True))

    class Meta:
        model = models.SubscriptionFeatures
        fields = '__all__'


class AddIndividualPackageFeatureForm(forms.ModelForm):
    class Meta:
        model = models.SubscriptionFeatures
        fields = ['feature_name', 'feature']


class EventCreateForm(forms.ModelForm):
    date_time = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'])

    # time_field = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'time'}),
    #                                  input_formats=['%H:%M', '%I:%M%p', '%I:%M %p'])

    class Meta:
        model = models.Events
        fields = '__all__'
        # exclude = ('event_image',)
# class EventPictureForm(forms.ModelForm):
#     profile_pic = forms.ImageField(widget=forms.FileInput)
#     class Meta:
#         model = models.Events
#         fields = ['event_image']

class OrderPriceForm(forms.ModelForm):
    class Meta:
        model = models.OrderPrice
        fields = ['initial_price', 'discount', 'processing_fee', 'tax', 'currency', 'payment_method'] #, 'invoice'
        widgets = {
            'discount': forms.NumberInput(attrs={'max': '100'}),
            'currency': forms.Select(attrs={'class': 'form-select'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
            'invoice': forms.FileInput(attrs={'class': 'form-control'})
        }


class QuotationForm(forms.ModelForm):
    class Meta:
        model = models.Quotation
        # fields = '__all__'
        exclude = ['category_choice', 'order', 'agreement']


class QuotationAgreementForm(forms.ModelForm):
    class Meta:
        model = models.QuotationAgreement
        exclude = ['quotation']


class OrderAssignForm(forms.ModelForm):
    staff = forms.ModelChoiceField(
        queryset=models.User.objects.filter(
            Q(is_staff=True, is_sales=True) | Q(is_superuser=True) | Q(is_staff=True, is_sales_head=True)),
        widget=forms.Select(attrs={'class': 'js-example-basic-single form-control form-select'}))

    class Meta:
        model = models.OrderStaff
        fields = ['staff', ]


class TicketCreateForm(forms.ModelForm):
    ticket_category = forms.Field(
        widget=forms.Select(attrs={'class': 'form-select'}))
    ticket_attachment = forms.FileField(widget=forms.FileInput(attrs={'accept': 'image/*,video/*,audio/*,.pdf,.csv'}),required=False)

    class Meta:
        model = models.Ticket
        fields = ['ticket_title', 'ticket_category', 'issue_category',
                  'ticket_description', 'ticket_attachment']
        # exclude = ['category_choice', 'ticket_status']


class TicketCommentForm(forms.ModelForm):
    class Meta:
        model = models.TicketComment
        fields = ['comment']


class BusinessLogoForm(forms.ModelForm):
    class Meta:
        model = models.Business
        fields = ['company_logo']


class BusinessInfoForm(forms.ModelForm):
    # industry_type = forms.Field(widget=forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = models.Business
        exclude = ['company_logo', 'unique_id']
        widgets = {
            'industry_type': forms.Select(attrs={'class': 'form-select'})
        }


class AssignToServiceForm(forms.ModelForm):
    class Meta:
        model = models.ServiceAssigned
        fields = ['service']
        widgets = {
            'service': forms.SelectMultiple(attrs={'class': 'js-example-basic-multiple'})
        }


class NotificationForm(forms.ModelForm):
    # category_choice = forms.ChoiceField(label='Select Target Users', choices=models.category_choice)
    notification_time = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'], widget=forms.TextInput(
        attrs={'value': dateformat.format(timezone.now(), 'Y/m/d H:i')}))

    class Meta:
        model = models.Notification
        fields = '__all__'
        exclude = ['is_read']
