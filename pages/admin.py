from django.contrib import admin
from .models import Header


class HeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'status')


admin.site.register(Header, HeaderAdmin)
