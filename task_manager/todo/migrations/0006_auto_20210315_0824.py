# Generated by Django 3.1.7 on 2021-03-15 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20210314_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='item',
            new_name='name',
        ),
    ]