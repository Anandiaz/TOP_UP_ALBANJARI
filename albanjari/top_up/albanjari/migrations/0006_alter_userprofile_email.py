# Generated by Django 5.0.8 on 2024-11-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albanjari', '0005_alter_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]