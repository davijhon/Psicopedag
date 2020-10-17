from django.contrib import admin
from .models import ( 
    Header, 
    Contacto, 
    Suscriptor, 
    Web,
    RedesSociales,
    FreePdf
)

class HeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'status')


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre','correo', 'asunto', 'mensaje','estado','fecha_creacion',)
    search_fields = ['correo']



class SuscriptorAdmin(admin.ModelAdmin):
    list_display = ('correo','estado','fecha_creacion')
    search_fields = ['correo']


class WebAdmin(admin.ModelAdmin):
    list_display = ('nosotros','email','direccion','telefono','estado','fecha_creacion')
    search_fields = ['email']
   


class RedesSocialesAdmin(admin.ModelAdmin):
    list_display = ('facebook','twitter','instagram','estado','fecha_creacion')
    search_fields = ['facebook']


class PdfFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')


admin.site.register(Header, HeaderAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Web, WebAdmin)
admin.site.register(RedesSociales, RedesSocialesAdmin)
admin.site.register(Suscriptor, SuscriptorAdmin)
admin.site.register(FreePdf, PdfFileAdmin)