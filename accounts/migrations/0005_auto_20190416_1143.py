# Generated by Django 2.1.5 on 2019-04-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190416_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense_table',
            name='image',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
    ]