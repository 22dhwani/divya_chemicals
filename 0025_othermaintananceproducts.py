# Generated by Django 4.0.5 on 2022-06-30 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divyaChemicalsWeb', '0024_civilproducts_electricalproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='otherMaintananceProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mechanicalMaintananceProducts', models.TextField(blank=True, max_length=2000, null=True)),

            ],
        ),
    ]
