# Generated by Django 4.1.4 on 2022-12-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='content_es',
            field=models.TextField(null=True),
        ),
    ]
