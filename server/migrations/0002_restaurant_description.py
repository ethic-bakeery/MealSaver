# Generated by Django 4.1.13 on 2024-05-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='description',
            field=models.CharField(default='Nicest Food ever', max_length=100),
            preserve_default=False,
        ),
    ]
