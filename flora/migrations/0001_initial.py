# Generated by Django 4.1.5 on 2023-03-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('feedback_text', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='date_published')),
            ],
        ),
    ]
