from django.contrib import admin
from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('date_joined', )
    ordering = ('-date_joined',)
    date_hierarchy = 'date_joined'

    # fieldsets = (
    #     ("User Info", {
    #         'fields': ('username', 'email', 'date_joined')
    #     }),
    # )


admin.site.register(Account, AccountAdmin)

