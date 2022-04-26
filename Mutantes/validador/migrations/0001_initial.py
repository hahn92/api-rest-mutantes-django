# Generated by Django 4.0.4 on 2022-04-26 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mutant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('dna', models.TextField(blank=True, default='', max_length=500, null=True, verbose_name='DNA')),
                ('is_mutant', models.BooleanField(default=False, verbose_name='Es mutante')),
            ],
            options={
                'verbose_name': 'Mutante',
                'verbose_name_plural': 'Mutantes',
                'ordering': ('-id',),
                'permissions': (('view_all_mutants', 'Can view all mutant'),),
            },
        ),
    ]
