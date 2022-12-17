# Generated by Django 4.1.3 on 2022-12-03 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddy', '0012_alter_group_member_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessions', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='study_sessions',
            field=models.ManyToManyField(to='studybuddy.session'),
        ),
    ]