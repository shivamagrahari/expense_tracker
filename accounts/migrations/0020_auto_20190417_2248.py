# Generated by Django 2.1.5 on 2019-04-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20190417_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='Img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
