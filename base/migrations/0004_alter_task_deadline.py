# Generated by Django 4.1.4 on 2022-12-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_user_username_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
