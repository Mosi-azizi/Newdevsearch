# Generated by Django 4.0.2 on 2022-03-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_feautured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='feautured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
