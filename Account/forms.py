from django import forms
from Account import models
from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
)
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django_countries.widgets import CountrySelectWidget
from django_countries.fields import CountryField

from allauth.account.forms import LoginForm as LF
from django.db.models import Q


class RegistrationForm(UserCreationForm):
    # phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'style': ' border: 1px '
    #                                                                                'solid #000;border-radius: '
    #                                                                                '0;outline: 0;padding-left: '
    #                                                                                '5px;height: 35px;'}))
    #
    # country = CountryField().formfield(widget=CountrySelectWidget(attrs={'style': ' border: 1px '
    #                                                                               'solid #000;border-radius: '
    #                                                                               '0;outline: 0;padding-left: '
    #                                                                               '5px;height: 35px;'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'style': ' border: 1px '
                                                                                             'solid #000;border-radius: '
                                                                                             '0;outline: 0;padding-left: '
                                                                                             '5px;height: 35px;'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'style': ' border: 1px '
                                                                                                     'solid #000;border-radius: '
                                                                                                     '0;outline: 0;padding-left: '
                                                                                                     '5px;height: 35px;'}))

    class Meta:
        model = models.User
        fields = ['full_name', 'email',
                  'password1',
                  'password2', 'newsletter']
        widgets = {
            'gender': forms.Select(attrs={'style': ' border: 1px '
                                                   'solid #000;border-radius: '
                                                   '0;outline: 0;padding-left: '
                                                   '5px;height: 35px;'}),
            'full_name': forms.TextInput(attrs={'style': ' border: 1px '
                                                         'solid #000;border-radius: '
                                                         '0;outline: 0;padding-left: '
                                                         '5px;height: 35px;'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'style': ' border: 1px '
                                                                          'solid #000;border-radius: '
                                                                          '0;outline: 0;padding-left: '
                                                                          '5px;height: 35px;'}),
            'email': forms.EmailInput(attrs={'style': ' border: 1px '
                                                      'solid #000;border-radius: '
                                                      '0;outline: 0;padding-left: '
                                                      '5px;height: 35px;'}),
            'profile_pic': forms.FileInput(attrs={'style': ' border: 1px '
                                                           'solid #000;border-radius: '
                                                           '0;outline: 0;padding-left: '
                                                           '5px;height: 35px;'}),
            # 'newsletter': forms.CheckboxInput(attrs={'style': ''})

        }


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'style': ' border: 1px '
                                                                        'solid #000;border-radius: '
                                                                        '0;outline: 0;padding-left: '
                                                                        '5px;height: 35px;'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'style': ' border: 1px '
                                                                          'solid #000;border-radius: '
                                                                          '0;outline: 0;padding-left: '
                                                                          '5px;height: 35px;'}))

    class Meta:
        model = models.User
        fields = '__all__'


class LoginForm2(LF):
    # username = forms.EmailField(widget=forms.EmailInput(attrs={'style': ' border: 1px '
    #                                                                     'solid #000;border-radius: '
    #                                                                     '0;outline: 0;padding-left: '
    #                                                                     '5px;height: 35px;'}))
    # password = forms.CharField(widget=forms.PasswordInput(attrs={'style': ' border: 1px '
    #                                                                       'solid #000;border-radius: '
    #                                                                       '0;outline: 0;padding-left: '
    #                                                                       '5px;height: 35px;'}))

    class Meta:
        model = models.User
        fields = '__all__'


class SelectBCSPermissionForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=models.User.objects.filter(is_superuser=False, is_staff=False))

    # user = forms.ModelChoiceField(queryset=models.User.objects.filter(Q(is_superuser=False, is_staff=False) and Q(permission_user__admin_type='bcs_admin')))

    class Meta:
        model = models.Permissions
        fields = '__all__'
        exclude = ['admin_type', ]
        widgets = {
            'user': forms.Select(attrs={'class': 'js-example-basic-single form-control form-select'})
        }


class InterestForm(forms.ModelForm):
    class Meta:
        model = models.Interest
        fields = '__all__'
        exclude = ['user', ]


class CountryPhoneForm(forms.ModelForm):
    phone_number = PhoneNumberField(
        widget=PhoneNumberPrefixWidget())
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    # country = CountryField().formfield(widget=CountrySelectWidget(attrs={'style': ' border: 1px '
    #                                                                               'solid #000;border-radius: '
    #                                                                               '0;outline: 0;padding-left: '
    #                                                                               '5px;height: 35px;'}))

    class Meta:
        model = models.User
        fields = ['country', 'phone_number', 'birth_date', 'gender']
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'country': forms.TextInput(attrs={'style': 'display: none'}),
        }


class AddressForm(forms.ModelForm):
    address_one = forms.CharField(required=True)
    address_two = forms.CharField(required=False)
    city = forms.CharField(required=True)
    # zipcode = forms.IntegerField(required=True)
    country = forms.CharField(required=True)

    class Meta:
        model = models.User
        fields = ['address_one', 'address_two', 'city', 'zipcode', 'country']



# class BirthDateGenderForm(forms.ModelForm):
#     birth_date = forms.DateField(widget=forms.DateInput(attrs={'style': ' border: 1px '
#                                                                         'solid #000;border-radius: '
#                                                                         '0;outline: 0;padding-left: '
#                                                                         '5px;height: 35px;', 'type': 'date'}))
#
#     class Meta:
#         model = models.User
#         fields = ['birth_date', 'gender']
#         widgets = {
#             'gender': forms.Select(attrs={'style': ' border: 1px '
#                                                    'solid #000;border-radius: '
#                                                    '0;outline: 0;padding-left: '
#                                                    '5px;height: 35px;', 'class': 'form-select'})
#         }


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['full_name', 'phone_number', 'address_one', 'address_two', 'city', 'zipcode',
                  'country', 'birth_date', 'gender']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'})
        }


class ProfilePictureForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = models.User
        fields = ['profile_pic']
