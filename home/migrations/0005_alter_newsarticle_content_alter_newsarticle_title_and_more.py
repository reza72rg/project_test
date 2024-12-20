# Generated by Django 4.2.17 on 2024-12-10 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_softwareversion_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsarticle",
            name="content",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="newsarticle",
            name="title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="slideshow",
            name="company_website",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="slides",
                to="home.companywebsite",
            ),
        ),
        migrations.AlterField(
            model_name="softwareversion",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
