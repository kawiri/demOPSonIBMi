from django.contrib import admin
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','address','phone_number','created')
    list_display_links = ('pk','user','created')
    list_editable = ('address','phone_number')