# Generated by Django 4.1.1 on 2022-11-07 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0019_imagens'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagens',
            old_name='imagens',
            new_name='img',
        ),
    ]