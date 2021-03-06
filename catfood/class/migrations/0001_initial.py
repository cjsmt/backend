# Generated by Django 3.1.2 on 2020-11-20 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_creator_school_id', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=50)),
                ('course_description', models.CharField(max_length=512, null=True)),
                ('course_credit', models.IntegerField(default=0)),
                ('course_type', models.CharField(max_length=20)),
                ('course_start_time', models.DateTimeField()),
                ('course_end_time', models.DateTimeField()),
                ('course_avatar', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Teacher', 'Teacher'), ('TeachingAssistant', 'TeachingAssistant'), ('Principle', 'Principle')], max_length=64)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.course')),
            ],
        ),
    ]
