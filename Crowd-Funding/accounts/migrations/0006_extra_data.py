<<<<<<< HEAD
# Generated by Django 3.2.9 on 2021-11-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_reg_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='extra_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_profile', models.CharField(max_length=100)),
            ],
        ),
    ]
=======
# Generated by Django 3.2.9 on 2021-11-30 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_reg_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='extra_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_profile', models.CharField(max_length=100)),
            ],
        ),
    ]
>>>>>>> 4dfdc7fcbba1fb6c58b2f2ad419064b3e21c7d5d
