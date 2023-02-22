# Generated by Django 4.1.6 on 2023-02-19 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0008_alter_mapping_id_alter_modifier_modifier_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='modifiers',
            field=models.ManyToManyField(blank=True, to='menu.modifier'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sectionid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu.section'),
        ),
    ]