# Generated by Django 2.1.5 on 2019-04-18 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_remove_expense_table_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense_table',
            name='image',
        ),
        migrations.AddField(
            model_name='photo',
            name='expense',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.expense_table'),
        ),
    ]
