# Generated by Django 3.1.4 on 2021-01-19 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_articles_context'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='files'),
        ),
    ]