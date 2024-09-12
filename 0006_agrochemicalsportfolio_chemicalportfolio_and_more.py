# Generated by Django 4.0.5 on 2022-06-20 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divyaChemicalsWeb', '0005_contactquery'),
    ]

    operations = [
        migrations.CreateModel(
            name='agrochemicalsPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='chemicalPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='engieeringAutomobilesPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='fertilizerPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='foodPharmaPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='glassCeramicPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='metalPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='oilGasPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='powerWindPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='tyrePortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('order', models.SmallIntegerField()),
                ('image', models.ImageField(default='logo.png', upload_to='')),
            ],
        ),
    ]