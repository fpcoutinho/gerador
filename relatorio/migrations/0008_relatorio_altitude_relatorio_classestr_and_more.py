# Generated by Django 4.1.1 on 2022-11-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0007_remove_relatorio_qualificacao_profissional_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatorio',
            name='altitude',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='classestr',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='competencia',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='condambiente',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='condfuga',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='contpessoas',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='descatm',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='infleletro',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='movdoar',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='natmatcons',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='natmatpr',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='presagua',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='presfauna',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='presmofo',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='pressolidos',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='pressubst',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='radsolar',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='reseletr',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='solmecanicas',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='tempambiente',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='vento',
            field=models.CharField(default='', max_length=30),
        ),
    ]
