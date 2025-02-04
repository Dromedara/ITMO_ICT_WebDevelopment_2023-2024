# Generated by Django 4.2.7 on 2023-11-02 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0004_alter_reservation_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='seat',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reserved_by', to='flights.seat'),
        ),
    ]
