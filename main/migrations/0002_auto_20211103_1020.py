# Generated by Django 3.2.3 on 2021-11-03 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='comments',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='products',
            name='images',
            field=models.TextField(default=''),
        ),
    ]