# Generated by Django 4.0.5 on 2022-06-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divyaChemicalsWeb', '0008_blogpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heroImageLink', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='heroImageLink',
        ),
    ]
