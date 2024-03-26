from django.contrib import admin
from authAPI.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
# Register your models here.

class UserModelAdmin(BaseUserAdmin):

    list_display=('id','email','password','is_admin')
    list_filter= ('is_admin',)
    fieldsets=(
        ('User Credentials',{'fields':('email','password')}),
        ('Permissions',{'fields':('is_admin',)}),
    )

    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','password'),
        }),
    )
    search_fields=('email',)
    ordering=('id','email')
    filter_horizontal=()




admin.site.register(User,UserModelAdmin)