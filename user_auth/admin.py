from django.contrib import admin

from .models import UserProfile, SharedNews
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(SharedNews) #don't forget this line