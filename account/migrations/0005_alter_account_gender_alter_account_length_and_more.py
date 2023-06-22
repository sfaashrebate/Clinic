# Generated by Django 4.1.7 on 2023-06-22 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_account_length_alter_account_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], default='female', max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='length',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AlterField(
            model_name='account',
            name='weight',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
