# Generated by Django 4.1.1 on 2022-11-05 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0012_relatorio_advquadist_relatorio_ambientesofreu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatorio',
            name='capbarramento',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='continuidade',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='ensaiodefunc',
            field=models.CharField(default='Ensaio de funcionamento?', max_length=100),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='ensaiodetensao',
            field=models.CharField(default='Ensaio de tensão aplicada?', max_length=100),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='ia',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='ib',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='ic',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='protdps',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='protdr',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='protgeral',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='resistencia',
            field=models.CharField(default='Resistência de isolamento da instalação elétrica?', max_length=100),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='selvpelv',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='vab',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='van',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='vbc',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='vbn',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='vca',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='vcn',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relatorio',
            name='verificacao',
            field=models.CharField(default='', max_length=100),
        ),
    ]
