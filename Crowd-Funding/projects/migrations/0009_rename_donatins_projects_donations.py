# Generated by Django 3.2.9 on 2021-11-25 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_projectimages_projects_projecttags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='donatins',
            new_name='donations',
        ),
    ]
