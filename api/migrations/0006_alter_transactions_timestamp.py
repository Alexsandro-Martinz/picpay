# Generated by Django 4.2.7 on 2023-11-11 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_receiver_profile_transactions_receiver_profile_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
