# Generated by Django 4.0.5 on 2022-06-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divyaChemicalsWeb', '0015_homepage_homeourstrengthheading'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicesImage', models.CharField(max_length=2000)),
                ('servicesIcon', models.CharField(max_length=200)),
                ('servicesName', models.CharField(max_length=200)),
                ('servicesInfo', models.TextField(max_length=3000)),
            ],
        ),
    ]
