# Generated by Django 2.1.7 on 2019-03-30 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bb_user', '0003_usersessions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersessions',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='usersessions',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 16, 26, 20, 590116)),
        ),
    ]