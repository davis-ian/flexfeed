# Generated by Django 3.2.9 on 2021-12-07 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_alter_category_exercises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='exercises',
            field=models.ManyToManyField(related_name='categories', to='exercises.Exercise'),
        ),
    ]