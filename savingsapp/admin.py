from django.contrib import admin

from .models import Accounts, Ledgers

admin.site.register(Accounts)
admin.site.register(Ledgers)

# Register your models here.
