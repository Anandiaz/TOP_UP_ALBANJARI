# Generated by Django 5.0.8 on 2024-11-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("albanjari", "0002_topuppackage_agent_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="category_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="category_images/"
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(default=0, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]