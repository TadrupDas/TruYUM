# Generated by Django 4.0.4 on 2022-06-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('active', models.BooleanField()),
                ('launch_date', models.DateField()),
                ('category', models.CharField(max_length=250)),
                ('free_delivery', models.BooleanField()),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]
