from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','sobrenome')
    list_display_links = ('nome', 'sobrenome')


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)


