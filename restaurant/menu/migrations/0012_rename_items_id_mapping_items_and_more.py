# Generated by Django 4.1.6 on 2023-02-19 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0011_alter_item_modifiers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mapping',
            old_name='items_id',
            new_name='items',
        ),
        migrations.RenameField(
            model_name='mapping',
            old_name='mod_id',
            new_name='modifiers',
        ),
        migrations.RemoveField(
            model_name='item',
            name='modifiers',
        ),
    ]