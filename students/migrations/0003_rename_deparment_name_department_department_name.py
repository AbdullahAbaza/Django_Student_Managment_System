# Generated by Django 5.0.6 on 2024-06-19 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_alter_department_table_alter_student_table"),
    ]

    operations = [
        migrations.RenameField(
            model_name="department",
            old_name="deparment_name",
            new_name="department_name",
        ),
    ]
