# Generated by Django 4.2.9 on 2024-01-11 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_alter_data_added_alter_data_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='published',
            field=models.DateTimeField(),
        ),
    ]
