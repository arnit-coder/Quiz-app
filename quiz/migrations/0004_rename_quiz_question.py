# Generated by Django 3.2.12 on 2022-10-13 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_remove_quiz_question_num'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quiz',
            new_name='Question',
        ),
    ]