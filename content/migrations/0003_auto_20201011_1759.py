# Generated by Django 3.0.7 on 2020-10-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20201010_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='deleted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]