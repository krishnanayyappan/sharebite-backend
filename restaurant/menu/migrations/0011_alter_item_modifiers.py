# Generated by Django 4.1.6 on 2023-02-19 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_rename_item_id_item_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='modifiers',
            field=models.ManyToManyField(blank=True, related_name='modifiers', to='menu.modifier'),
        ),
    ]
