# Generated by Django 3.2.23 on 2023-11-24 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'about us', 'verbose_name_plural': 'abous us'},
        ),
        migrations.AlterModelOptions(
            name='chef',
            options={'verbose_name': 'chef', 'verbose_name_plural': 'chef'},
        ),
        migrations.AlterModelOptions(
            name='why_choose_us',
            options={'verbose_name': 'why choose us', 'verbose_name_plural': 'why choose us'},
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='image',
        ),
    ]
