# Generated by Django 4.1.1 on 2022-09-27 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_answer_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='number_of_appearances',
            field=models.IntegerField(default=0),
        ),
    ]
