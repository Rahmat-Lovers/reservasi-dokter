from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from main.models import Customer, Doctor, Schedule, Specialist

class AdminSite(admin.AdminSite):
    pass

admin_site = AdminSite()

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Customer)
admin_site.register(Doctor)
admin_site.register(Schedule)
admin_site.register(Specialist)