# Generated by Django 3.1.4 on 2020-12-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
