# Generated by Django 3.2 on 2023-01-09 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='nome',
            new_name='cliente',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tel02',
            field=models.CharField(max_length=60, null=True, verbose_name='Tel. Residencial'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='tel02',
            field=models.CharField(max_length=60, null=True, verbose_name='Tel. Residencial'),
        ),
    ]
