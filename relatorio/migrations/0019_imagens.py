# Generated by Django 4.1.1 on 2022-11-07 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0018_rename_descrição_circuito_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.FileField(blank=True, null=True, upload_to='media/')),
                ('rel_pai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relatorio.relatorio')),
            ],
        ),
    ]
