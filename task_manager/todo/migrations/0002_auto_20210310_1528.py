# Generated by Django 3.1.7 on 2021-03-10 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='points',
            field=models.IntegerField(blank=True, default=25, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='work_time',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='item',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='time_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
