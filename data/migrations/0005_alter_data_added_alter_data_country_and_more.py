# Generated by Django 4.2.9 on 2024-01-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_data_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='added',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='end_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='impact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='insight',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='likelihood',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='pestle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='region',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='relevance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='sector',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='source',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='start_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='data',
            name='topic',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.URLField(),
        ),
    ]
