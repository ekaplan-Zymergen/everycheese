# Generated by Django 3.0.8 on 2020-07-17 18:42

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0002_cheese_firmness'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheese',
            name='country_of_origin',
            field=django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country of Origin'),
        ),
    ]
