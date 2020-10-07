from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','sobrenome','telefone','mostrar')
    list_display_links = ('nome','sobrenome')
    list_editable = ('telefone','mostrar')


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)


