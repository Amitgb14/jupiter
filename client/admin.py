# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Country, State, City, User, Message


def mark_enable(obj, request, queryset):
        rows_update=queryset.update(status=1)
        mm(obj,rows_update, request,"Enable")
def mark_disable(obj, request, queryset):
        rows_update=queryset.update(status=0)
        mm(obj,rows_update, request,"Disable")
mark_enable.short_description="Enable"
mark_disable.short_description="Disable"

def mm(obj,rows_update, request, work):
       if rows_update==1:
          msg="1 story was"
       else:
          msg="%s stories were" % rows_update
       obj.message_user(request,"%s successfully as %s." % (msg, work))

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'status')
admin.site.register(Country, CountryAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'country', 'status')
admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'state', 'status')
admin.site.register(City, CityAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'contact_no', 'status')
admin.site.register(User, UserAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'read', 'date', 'status')
admin.site.register(Message, MessageAdmin)
