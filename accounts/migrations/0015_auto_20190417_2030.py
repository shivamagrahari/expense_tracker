# Generated by Django 2.1.5 on 2019-04-17 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20190417_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='expense_table',
            name='Img',
        ),
        migrations.AddField(
            model_name='expense_table',
            name='image',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.photo'),
        ),
    ]
