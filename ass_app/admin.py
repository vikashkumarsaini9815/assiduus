
from django.contrib import admin
from .models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display= ['id','username','email','Token']
    search_fields = ['username',]
admin.site.register(User, UserAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display= ['id','message','created','updated']
admin.site.register(Message, MessageAdmin)