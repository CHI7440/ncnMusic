# Generated by Django 5.0.1 on 2024-01-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Face_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d/')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
    ]
