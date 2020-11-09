from django.contrib import admin
from .models import ( 
    Header, 
    Contacto, 
    Suscriptor, 
    Web,
    RedesSociales,
    Toolbox,
    Feature,
    Section,
    SectionContent,
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


class SectionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('seccion', 'caracteristica',)

class SectionContentAdmin(admin.ModelAdmin):
    list_display = ('seccion', 'created',)



admin.site.register(Header, HeaderAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Web, WebAdmin)
admin.site.register(RedesSociales, RedesSocialesAdmin)
admin.site.register(Suscriptor, SuscriptorAdmin)
admin.site.register(Toolbox, PdfFileAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(SectionContent, SectionContentAdmin)
admin.site.register(Section, SectionAdmin)
