# Generated by Django 2.1.5 on 2019-04-16 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190413_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense_table',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
