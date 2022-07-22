from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse
from Account import models, forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from allauth.socialaccount.models import SocialAccount


# Create your views here.
def login_executed(redirect_to):
    """This Decorator kicks authenticated user out of a view"""

    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(redirect_to)
            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper


# @login_executed('account_app:profile')
# def signupView(request):
#     form = forms.RegistrationForm()
#     if request.method == 'POST':
#         form = forms.RegistrationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return HttpResponseRedirect(reverse('account_app:profile'))
#     context = {
#         'form': form,
#     }
#     return render(request, 'account/signup.html', context)
#
#
# @login_executed('account_app:profile')
# def loginView(request):
#     form = forms.LoginForm()
#     next_url = ''
#     if request.method == 'POST':
#         form = forms.LoginForm(data=request.POST)
#         username, password = request.POST.get('username'), request.POST.get('password')
#         next_url = request.GET.get('next')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 if next_url:
#                     return redirect(next_url)
#                 else:
#                     return HttpResponseRedirect(reverse('account_app:profile'))
#     context = {
#         'form': form,
#     }
#     return render(request, 'account/login.html', context)

@login_required
def profileView(request):
    current_user = request.user
    interests = models.Interest.objects.get(user=current_user)
    img_forms = forms.ProfilePictureForm(instance=request.user)

    email_verify = request.user.emailaddress_set.all()

    def userFunc():
        form = forms.InterestForm(instance=interests)
        if not current_user.phone_number \
                or not current_user.address_one \
                or not current_user.city \
                or not current_user.zipcode \
                or not current_user.country \
                or not current_user.birth_date \
                or not current_user.gender:

            if not current_user.phone_number \
                    or not current_user.country \
                    or not current_user.birth_date \
                    or not current_user.gender:
                form = forms.CountryPhoneForm(instance=current_user)
                message = 'Fill your information below.'
                success = 'Please provide these information:'
                if request.POST:
                    form = forms.CountryPhoneForm(request.POST, instance=current_user)
                    if form.is_valid():
                        form.save()
                        return HttpResponseRedirect(reverse('user_profile'))
                context = {
                    'form': form,
                    'message': message,
                    'success': success,
                    'title': 'Basic Info',
                }
                return render(request, 'account/profile-info-add.html', context)
            elif not current_user.address_one \
                    or not current_user.city \
                    or not current_user.zipcode:
                form = forms.AddressForm(instance=current_user)
                message = 'Fill your information below.'
                success = 'Please provide these information:'
                if request.POST:
                    form = forms.AddressForm(request.POST, instance=current_user)
                    if form.is_valid():
                        form.save()
                        return HttpResponseRedirect(reverse('user_profile'))
                context = {
                    'form': form,
                    'message': message,
                    'success': success,
                    'title': 'Basic Info',
                }
                return render(request, 'account/profile-info-add.html', context)
        else:
            # print(current_user.profile_pic)
            if request.method == 'POST':
                if 'img-btn' in request.POST:
                    form = forms.ProfilePictureForm(request.POST, request.FILES, instance=request.user)
                    if form.is_valid():
                        form.save()
                        return redirect('user_profile')
            
                # form = forms.InterestForm(request.POST, instance=interests)
                # if form.is_valid():
                #     form.save()
                #     return HttpResponseRedirect(reverse('user_profile'))
            try:
                social_account = current_user.socialaccount_set.filter(provider='google')[0]
                if not current_user.full_name:
                    current_user.full_name = social_account.extra_data['name']
                    # current_user.profile_pic = social_account.extra_data['picture']
                    current_user.save()
            except:
                pass
            # val=[]
            # for field in interests._meta.fields:
            #     val.append(field.get_attname_column()[0])

            # print(val)
            # print(interests.risk_assessment)
            # for x in val:
            #    print(interests+"."+x)
            context = {
                # 'vals': val,
                'img_forms': img_forms,
                'interests': interests,
                'form': form,
                
            }
            return render(request, 'account/profile.html', context)

    if email_verify.exists():
        for email in email_verify:
            if not email.verified:
                message = 'Email Unverified. Please Check your Email Inbox/Spam Folder for Verification Link'
                context = {
                    'message': message,
                    'title': 'Confirm Email',
                }
                return render(request, 'account/profile-info-add.html', context)
            else:
                return userFunc()
    else:
        return userFunc()


# @login_required
# def profileView(request):
#     current_user = request.user
#     interests = models.Interest.objects.get(user=current_user)
#     form = forms.InterestForm(instance=interests)
#     email_verify = request.user.emailaddress_set.all()
#     for email in email_verify:
#         if not email.verified:
#             message = 'Email Unverified. Please Check your Email Inbox/Spam Folder for Verification Link'
#             context = {
#                 'message': message,
#             }
#             return render(request, 'account/profile-info-add.html', context)
#         else:
#             if not current_user.phone_number \
#                     or not current_user.country \
#                     or not current_user.phone_number \
#                     or not current_user.birth_date \
#                     or not current_user.gender:
#
#                 emails = current_user.emailaddress_set.all
#                 if not current_user.phone_number \
#                         or not current_user.country:
#                     form = forms.CountryPhoneForm(instance=current_user)
#                     message = 'Add Country and Phone Number'
#                     if request.POST:
#                         form = forms.CountryPhoneForm(request.POST, instance=current_user)
#                         if form.is_valid():
#                             form.save()
#                             return HttpResponseRedirect(request.META['HTTP_REFERER'])
#                 elif not current_user.birth_date \
#                         or not current_user.gender:
#                     form = forms.BirthDateGenderForm(instance=current_user)
#                     message = 'Add Date of Birth and Gender'
#                     if request.POST:
#                         form = forms.BirthDateGenderForm(request.POST, instance=current_user)
#                         if form.is_valid():
#                             form.save()
#                             return HttpResponseRedirect(request.META['HTTP_REFERER'])
#                 context = {
#                     'emails': emails,
#                     'form': form,
#                     'message': message,
#                 }
#                 return render(request, 'account/profile-info-add.html', context)
#             else:
#                 if request.method == 'POST':
#                     form = forms.InterestForm(request.POST, instance=interests)
#                     if form.is_valid():
#                         form.save()
#                         return HttpResponseRedirect(request.META['HTTP_REFERER'])
#                 context = {
#                     # 'interests': interests,
#                     'form': form,
#                 }
#                 return render(request, 'account/profile.html', context)


@login_required
def profileEdit(request):
    info_forms = forms.ProfileInfoForm(instance=request.user)
    img_forms = forms.ProfilePictureForm(instance=request.user)
    interests = models.Interest.objects.get(user=request.user)
    int_forms = forms.InterestForm(instance=interests)
    if request.method == 'POST':
        if 'info-btn' in request.POST:
            info_forms = forms.ProfileInfoForm(request.POST, instance=request.user)
            if info_forms.is_valid():
                info_forms.save()
                return redirect('user_profile')
        elif 'img-btn' in request.POST:
            img_forms = forms.ProfilePictureForm(request.POST, request.FILES, instance=request.user)
            if img_forms.is_valid():
                img_forms.save()
                return redirect('user_profile')
        elif 'int-btn' in request.POST:
            int_forms = forms.InterestForm(request.POST, instance=interests)
            if int_forms.is_valid():
                int_forms.save()
                return redirect('user_profile')
    context = {
        'info_forms': info_forms,
        'img_forms': img_forms,
        'int_forms': int_forms,
    }
    return render(request, 'account/profile_edit.html', context)


@login_required
def passwordChangeView(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_profile'))

    context = {
        'form': form,
    }
    return render(request, 'account/change_password.html', context)


@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
