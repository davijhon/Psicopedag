from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import ( 
    Header, 
    Contacto, 
    Web,
    RedesSociales,
    Toolbox,
    Feature,
    Section,
    SectionContent,
)

class HeaderResource(resources.ModelResource):
    class Meta:
        model = Header


class ContactoResource(resources.ModelResource):
    class Meta:
        model = Contacto


class WebResource(resources.ModelResource):
    class Meta:
        model = Web


class RedesSocialesResource(resources.ModelResource):
    class Meta:
        model = RedesSociales


class SectionResource(resources.ModelResource):
    class Meta:
        model = Section


class FeatureResource(resources.ModelResource):
    class Meta:
        model = Feature


class SectionContentResource(resources.ModelResource):
    class Meta:
        model = SectionContent


class PdfFileResource(resources.ModelResource):
    class Meta:
        model = Toolbox


class HeaderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'position', 'status')
    resource_class = HeaderResource


class ContactoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre','correo', 'asunto', 'mensaje','estado','fecha_creacion',)
    search_fields = ['correo']
    resource_class = ContactoResource


class WebAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nosotros','email','direccion','telefono','estado','fecha_creacion')
    search_fields = ['email']
    resource_class = WebResource


class RedesSocialesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('facebook','twitter','instagram','estado','fecha_creacion')
    search_fields = ['facebook']
    resource_class = RedesSocialesResource


class PdfFileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    resource_class = PdfFileResource


class SectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre',)
    resource_class = SectionResource


class FeatureAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('seccion', 'caracteristica',)
    resource_class = FeatureResource


class SectionContentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('seccion', 'created',)
    resource_class = SectionContentResource


admin.site.register(Header, HeaderAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Web, WebAdmin)
admin.site.register(RedesSociales, RedesSocialesAdmin)
admin.site.register(Toolbox, PdfFileAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(SectionContent, SectionContentAdmin)
admin.site.register(Section, SectionAdmin)
