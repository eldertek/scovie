# Generated by Django 4.1.5 on 2023-03-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('screen', '0002_configuration_carnival_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=50, verbose_name='teacher'),
        ),
    ]
