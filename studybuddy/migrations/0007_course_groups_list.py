# Generated by Django 4.1.1 on 2022-11-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0006_user_courselist_user_groupslist'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='groups_list',
            field=models.ManyToManyField(to='studybuddy.group'),
        ),
    ]
