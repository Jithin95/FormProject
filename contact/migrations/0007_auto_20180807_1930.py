# Generated by Django 2.1 on 2018-08-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_surveymodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveymodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
