# Generated by Django 4.1.3 on 2022-12-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0013_session_group_study_sessions'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_sub',
            field=models.CharField(default='NULL', max_length=300),
        ),
    ]
