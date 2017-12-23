from django.contrib import admin
from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    pass


admin.site.register(Account, AccountAdmin)

