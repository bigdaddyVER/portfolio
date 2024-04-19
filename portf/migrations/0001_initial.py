# Generated by Django 4.2.11 on 2024-04-06 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('pers_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='img/')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_initial', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=80)),
                ('desc', models.TextField()),
                ('age', models.CharField(max_length=5)),
                ('facebook_url', models.URLField(blank=True, max_length=255, null=True)),
                ('insta_url', models.URLField(blank=True, max_length=255, null=True)),
                ('email_add', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('col_year', models.CharField(max_length=50, null=True)),
                ('col_sch', models.CharField(max_length=50, null=True)),
                ('shs_year', models.CharField(max_length=50, null=True)),
                ('shs_sch', models.CharField(max_length=50, null=True)),
                ('jhs_year', models.CharField(max_length=50, null=True)),
                ('jhs_sch', models.CharField(max_length=50, null=True)),
                ('ele_year', models.CharField(max_length=50, null=True)),
                ('ele_sch', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
