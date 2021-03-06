# Generated by Django 3.2.14 on 2022-07-06 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=50)),
                ('place_name', models.CharField(max_length=50)),
                ('publishTime', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('place_url', models.CharField(max_length=50)),
                ('address_6', models.CharField(max_length=50)),
                ('viewCount', models.IntegerField()),
                ('likeCount', models.IntegerField()),
                ('x', models.DecimalField(decimal_places=18, max_digits=24)),
                ('y', models.DecimalField(decimal_places=18, max_digits=24)),
            ],
        ),
    ]
