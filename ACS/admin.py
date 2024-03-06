from django.contrib import admin
from .models import Record, AccountPayable, Payment,  Expense, Treasurer, MoneyTransfer
# Register your models here.

admin.site.register(Record)
admin.site.register(AccountPayable)
admin.site.register(Payment)
admin.site.register(Expense)
admin.site.register(Treasurer)
admin.site.register(MoneyTransfer)