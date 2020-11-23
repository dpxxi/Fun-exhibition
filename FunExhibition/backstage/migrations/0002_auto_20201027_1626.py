# Generated by Django 2.1.15 on 2020-10-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='time',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='time'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='artist_letter',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='艺术家字母'),
        ),
    ]
