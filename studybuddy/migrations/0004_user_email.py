# Generated by Django 4.1.1 on 2022-10-31 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0003_course_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='NULL', max_length=500),
        ),
    ]
