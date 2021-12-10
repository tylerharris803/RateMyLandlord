# Generated by Django 3.2.8 on 2021-12-10 18:09

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('management_company', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'ratemylandlord_landlord',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('zipcode', models.CharField(max_length=10)),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ratemylandlord.landlord')),
            ],
            options={
                'db_table': 'ratemylandlord_property',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'ratemylandlord_user',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('poor_management', models.BooleanField(default=False)),
                ('hidden_fees', models.BooleanField(default=False)),
                ('lack_of_privacy', models.BooleanField(default=False)),
                ('unreturned_funds', models.BooleanField(default=False)),
                ('property_condition', models.CharField(max_length=50)),
                ('utilities', models.BooleanField(default=False)),
                ('safety_concerns', models.BooleanField(default=False)),
                ('appliance_issues', models.BooleanField(default=False)),
                ('mold', models.BooleanField(default=False)),
                ('pests', models.BooleanField(default=False)),
                ('neighborhood_problems', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('bad_contracts', models.BooleanField(default=False)),
                ('change_in_rent', models.BooleanField(default=False)),
                ('other_notes', models.CharField(max_length=5000)),
                ('date_submitted', models.DateField(blank=True, default=datetime.datetime.today)),
                ('properties', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ratemylandlord.property')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ratemylandlord.user')),
            ],
            options={
                'db_table': 'ratemylandlord_rating',
            },
        ),
    ]
