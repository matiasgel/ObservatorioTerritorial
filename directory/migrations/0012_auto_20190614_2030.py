# Generated by Django 2.2 on 2019-06-14 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0011_auto_20190614_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='document',
            field=models.FileField(upload_to='publicaciones'),
        ),
    ]