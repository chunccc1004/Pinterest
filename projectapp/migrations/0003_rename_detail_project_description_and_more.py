# Generated by Django 4.2.9 on 2024-01-28 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_rename_writer_project_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='detail',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='title',
        ),
    ]