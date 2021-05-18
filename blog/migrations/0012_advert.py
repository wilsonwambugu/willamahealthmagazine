# Generated by Django 3.2 on 2021-05-09 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adv', models.ImageField(blank=True, null=True, upload_to='ads/')),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
