# Generated by Django 4.2.7 on 2023-11-10 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='receiver_profile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='sender_profile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
