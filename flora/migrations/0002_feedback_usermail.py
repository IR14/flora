# Generated by Django 4.1.5 on 2023-03-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='usermail',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
