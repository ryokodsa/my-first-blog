# Generated by Django 2.2.24 on 2021-10-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20211027_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='seat',
            field=models.CharField(default='A', max_length=10),
            preserve_default=False,
        ),
    ]