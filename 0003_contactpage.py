# Generated by Django 4.0.5 on 2022-06-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divyaChemicalsWeb', '0002_homepage_hometestimonialauthor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heroImageLink', models.CharField(max_length=10000)),
                ('address', models.TextField(max_length=10000)),
                ('contact', models.CharField(max_length=10000)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
