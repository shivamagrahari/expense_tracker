# Generated by Django 2.1.5 on 2019-04-18 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20190418_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='expense',
        ),
        migrations.AddField(
            model_name='expense_table',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.photo'),
        ),
    ]
