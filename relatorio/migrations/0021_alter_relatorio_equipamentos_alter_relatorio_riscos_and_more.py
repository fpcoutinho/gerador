# Generated by Django 4.1.1 on 2022-11-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0020_rename_imagens_imagens_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorio',
            name='equipamentos',
            field=models.CharField(default='[]', max_length=100),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='riscos',
            field=models.CharField(default='[]', max_length=100),
        ),
        migrations.AlterField(
            model_name='relatorio',
            name='sinalizacao',
            field=models.CharField(default='[]', max_length=100),
        ),
    ]
