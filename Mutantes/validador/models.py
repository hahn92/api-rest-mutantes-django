# Django
from django.db import models
# Solo con postgres
# from django.contrib.postgres.fields import JSONField

# Create your models here.

class TemplateValidador(models.Model):

    is_active = models.BooleanField(
        default=True,
        verbose_name='Activo',
    )
    # Logs
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creado'
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name='Modificado'
    )

    class Meta:
        abstract = True


class Mutant(TemplateValidador):

    dna = models.TextField(
        max_length=500,
        default="",
        blank=True,
        null=True,
        verbose_name='DNA',
    )

    is_mutant = models.BooleanField(
        default=False,
        verbose_name='Es mutante',
    )

    def __str__(self):
        return "{}: {}".format(self.id, self.is_mutant)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Mutante'
        verbose_name_plural = 'Mutantes'
        permissions = (
            ("view_all_mutants", "Can view all mutant"),
        )

