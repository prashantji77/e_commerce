# Generated by Django 5.0 on 2024-01-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAPI', '0002_alter_productcategory_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
