# Generated by Django 3.2 on 2021-05-12 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_lists'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lat_real',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Latest Releases'},
        ),
        migrations.AlterModelOptions(
            name='lists',
            options={'ordering': ['-created_on'], 'verbose_name_plural': 'Lists'},
        ),
    ]
