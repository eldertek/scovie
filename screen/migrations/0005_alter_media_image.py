# Generated by Django 4.1.5 on 2023-01-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screen', '0004_rename_content_media_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.FileField(upload_to='media/'),
        ),
    ]