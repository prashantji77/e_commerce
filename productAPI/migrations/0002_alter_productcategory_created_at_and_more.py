# Generated by Django 5.0 on 2024-01-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='categories',
            field=models.ManyToManyField(to='productAPI.productcategory'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
