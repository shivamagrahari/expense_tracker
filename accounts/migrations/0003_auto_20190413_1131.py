# Generated by Django 2.1.5 on 2019-04-13 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_expense_table_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense_table',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
