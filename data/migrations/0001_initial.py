# Generated by Django 4.2.9 on 2024-01-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.IntegerField()),
                ('intensity', models.IntegerField()),
                ('sector', models.CharField(blank=True, max_length=400, null=True)),
                ('topic', models.CharField(blank=True, max_length=400, null=True)),
                ('insight', models.CharField(blank=True, max_length=400, null=True)),
                ('url', models.CharField(blank=True, max_length=400, null=True)),
                ('region', models.CharField(blank=True, max_length=400, null=True)),
                ('start_year', models.IntegerField()),
                ('impact', models.CharField(blank=True, max_length=400, null=True)),
                ('added', models.DateTimeField()),
                ('published', models.DateTimeField()),
                ('country', models.CharField(blank=True, max_length=400, null=True)),
                ('relevance', models.IntegerField()),
                ('pestle', models.CharField(blank=True, max_length=400, null=True)),
                ('source', models.CharField(blank=True, max_length=400, null=True)),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('likelihood', models.IntegerField()),
            ],
        ),
    ]
