# Generated by Django 4.2.7 on 2023-11-10 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('document', models.CharField(max_length=255, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=11)),
                ('profile_type', models.CharField(choices=[('COMMON', 'Common'), ('MERCHANT', 'Merchant')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_created=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('receiver_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_profile', to='api.profile')),
                ('sender_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_profile', to='api.profile')),
            ],
        ),
    ]
