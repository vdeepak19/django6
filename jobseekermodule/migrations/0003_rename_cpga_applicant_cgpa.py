# Generated by Django 5.0.1 on 2024-01-31 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseekermodule', '0002_alter_applicant_cpga'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='cpga',
            new_name='cgpa',
        ),
    ]