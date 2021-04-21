from django.contrib import admin
from users.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','address','phone_number','created')
    list_display_links = ('pk','user','created')
    list_editable = ('address','phone_number')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user','photo'),
                ('sex')),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography'),
                ('address','city','country')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )
    readonly_fields = ('created', 'modified',)