# Generated by Django 4.1.4 on 2022-12-11 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
