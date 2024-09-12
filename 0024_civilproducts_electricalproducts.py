# Generated by Django 4.0.5 on 2022-06-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divyaChemicalsWeb', '0023_mechanicalproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='civilProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilProductImage', models.ImageField(default='logo.png', upload_to='')),
                ('civilProductImageName', models.CharField(max_length=2000)),
                ('civilProductsImageDescription', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='electricalProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electricalProductImage', models.ImageField(default='logo.png', upload_to='')),
                ('electricalProductImageName', models.CharField(max_length=2000)),
                ('electricalProductsImageDescription', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]