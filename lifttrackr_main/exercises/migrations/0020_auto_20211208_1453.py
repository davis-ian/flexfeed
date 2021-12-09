# Generated by Django 3.2.9 on 2021-12-08 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0019_alter_setinstance_exerciseinstance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setinstance',
            name='exerciseinstance',
        ),
        migrations.AddField(
            model_name='setinstance',
            name='exerciseinstance',
            field=models.ManyToManyField(related_name='setinstance', to='exercises.ExerciseInstance'),
        ),
    ]
