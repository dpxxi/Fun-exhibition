# Generated by Django 2.1.15 on 2020-10-28 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backstage', '0004_auto_20201028_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='user_img/user.png', upload_to='user_img'),
        ),
    ]
