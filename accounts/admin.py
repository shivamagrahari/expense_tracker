from django.contrib import admin
from .models import expense_table, photo


# Register your models here.

admin.site.register(expense_table)
admin.site.register( photo)
