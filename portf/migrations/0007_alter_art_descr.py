# Generated by Django 4.2.1 on 2024-04-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portf', '0006_rename_title_art_descr_alter_website_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='descr',
            field=models.TextField(),
        ),
    ]
