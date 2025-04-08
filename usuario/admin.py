from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16


class UsuarioDS16Admin(UserAdmin):
    list_display = ('telefone',)  # vírgula para tornar tupla

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefone',)}),  # vírgula para tupla
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telefone',)}),  # vírgula aqui também
    )

admin.site.register(UsuarioDS16, UsuarioDS16Admin)
