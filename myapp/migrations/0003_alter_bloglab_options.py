# Generated by Django 4.1.3 on 2023-01-25 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_user_bloglab'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloglab',
            options={'ordering': ['-created_on']},
        ),
    ]
