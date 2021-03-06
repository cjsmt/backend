# Generated by Django 3.1.2 on 2020-11-20 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('class', '0002_auto_20201121_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeworkScoreList',
            fields=[
                ('homework_id', models.AutoField(primary_key=True, serialize=False)),
                ('homework_student_grade', models.IntegerField()),
                ('homework_teachers_comments', models.CharField(max_length=2048)),
                ('homework_is_grade_available_to_students', models.BooleanField(default=False)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkList',
            fields=[
                ('homework_id', models.AutoField(primary_key=True, serialize=False)),
                ('homework_description', models.CharField(max_length=1024)),
                ('homework_attachment_link', models.CharField(max_length=200)),
                ('homework_start_timestamp', models.DateTimeField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.course')),
                ('homework_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkFileList',
            fields=[
                ('file_homework_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_usage', models.CharField(choices=[('Experiment', 'Experiment'), ('Lecture', 'Lecture')], max_length=100)),
                ('file_timestamp', models.DateField(auto_now=True)),
                ('file_link', models.CharField(max_length=200)),
                ('file_uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('homework_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecture.homeworklist')),
            ],
        ),
    ]
