# Generated by Django 3.1.2 on 2020-11-20 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teach',
            name='teacher_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AlterUniqueTogether(
            name='teach',
            unique_together={('teacher_id', 'course_id')},
        ),
    ]