# Generated by Django 4.1.1 on 2022-11-05 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0014_alter_relatorio_continuidade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatorio',
            name='circuito',
            field=models.CharField(default='', max_length=100),
        ),
    ]
