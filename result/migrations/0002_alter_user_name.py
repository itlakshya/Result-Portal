# Generated by Django 4.2.2 on 2023-06-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]