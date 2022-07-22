from django.contrib import admin
from Account.models import User, Permissions, Interest
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class AdminUser(UserAdmin):
    ordering = ('-date_joined',)
    search_fields = ('email', 'full_name', 'phone_number',)
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'gender', 'is_bcs',)
    list_display = ('email', 'full_name', 'country', 'gender', 'date_joined', 'is_bcs', 'is_active')
    fieldsets = (
        ('Login Info', {'fields': ('email', 'password')}),
        ('User Information',
         {'fields': ('full_name', 'gender', 'profile_pic', 'birth_date', 'address_one', 'address_two', 'city', 'zipcode',
                     'country', 'phone_number',)}),
        ('Permissions', {'fields': ('is_bcs', 'is_active', 'is_staff', 'is_superuser', 'is_sales_head', 'is_sales',
                                    'is_blogger', 'is_bcs_head', 'is_pcs_head', 'newsletter',)}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )


admin.site.register(User, AdminUser)
admin.site.register(Permissions)
admin.site.register(Interest)
