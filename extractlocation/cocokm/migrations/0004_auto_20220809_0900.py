# Generated by Django 3.2.14 on 2022-08-09 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocokm', '0003_auto_20220809_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='placeThumbnail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='videoThumbnail',
            field=models.TextField(),
        ),
    ]