# Generated by Django 4.1.1 on 2022-09-28 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0004_relatorio_altura_relatorio_aterramento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relatorio',
            old_name='qualiprofi',
            new_name='Qualificacao_Profissional',
        ),
    ]
