# Generated by Django 2.1.5 on 2019-04-18 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20190417_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='Img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]
