# Generated by Django 4.0.5 on 2022-06-24 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divyaChemicalsWeb', '0013_homeheroimage_remove_homepage_blogauthor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homeTestimonialImage', models.ImageField(default='2.png', upload_to='')),
                ('homeTestimonialAuthor', models.TextField(max_length=200, null=True)),
                ('homeTestimonialDesignation', models.CharField(max_length=200, null=True)),
                ('homeTestimonialContent', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='homeTestimonialAuthor',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='homeTestimonialContent',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='homeTestimonialDesignation',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='homeTestimonialImage',
        ),
        migrations.AddField(
            model_name='homepage',
            name='homeProductsDescription',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]