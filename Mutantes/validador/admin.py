from django.contrib import admin

# Models
from .models import Mutant

@admin.register(Mutant)
class MutantAdmin(admin.ModelAdmin):
    """
    Vista Tasks en administrador
    """
    list_display = ('pk', 'is_mutant',  'created', 'modified')
    list_display_links = ('pk', 'is_mutant', 'created', 'modified')

    search_fields = (
        'dna',
    )

    list_filter = (
        'is_mutant',
        'is_active',
        'created',
        'modified',
    )

    fieldsets = (
        ('Datos basicos', {
            'fields': (
                ( 'dna', 'is_active', 'is_mutant',),
            ),
        }),
        ('Metadatos', {
            'fields': ('created', 'modified',),
        })
    )

    readonly_fields = ('created', 'modified',)
