# Generated by Django 4.2.4 on 2023-08-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
