# Generated by Django 4.2.16 on 2024-12-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_softwareversion_software_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="softwareversion",
            name="download_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
