# Generated by Django 5.0.6 on 2024-07-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=200),
        ),
    ]