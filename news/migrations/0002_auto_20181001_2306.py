# Generated by Django 2.1.1 on 2018-10-01 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='body',
            new_name='post',
        ),
    ]
