# Generated by Django 4.1.3 on 2022-12-01 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compyterstats', '0002_alter_computer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='datetime_captured',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='date captured'),
        ),
    ]