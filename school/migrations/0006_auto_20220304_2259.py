# Generated by Django 3.1.2 on 2022-03-04 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20220304_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='school.teacher'),
            preserve_default=False,
        ),
    ]
