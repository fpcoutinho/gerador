# Generated by Django 4.1.1 on 2022-10-07 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0005_rename_qualiprofi_relatorio_qualificacao_profissional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatorio',
            name='especialista',
        ),
        migrations.RemoveField(
            model_name='relatorio',
            name='nome',
        ),
    ]
