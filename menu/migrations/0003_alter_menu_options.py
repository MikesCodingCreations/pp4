# Generated by Django 3.2.22 on 2023-10-24 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'menu', 'verbose_name_plural': 'menus'},
        ),
    ]
