# Generated by Django 3.1.2 on 2020-11-20 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('university_id', models.AutoField(primary_key=True, serialize=False)),
                ('university_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('password_digest', models.CharField(max_length=50)),
                ('realname', models.CharField(max_length=50)),
                ('school_id_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('university_id', models.IntegerField()),
                ('school_id', models.IntegerField()),
                ('character', models.CharField(choices=[('Teacher', 'Teacher'), ('TeachingAssistant', 'TeachingAssistant')], max_length=32)),
                ('avatar', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=50)),
                ('university_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.university')),
            ],
        ),
        migrations.CreateModel(
            name='TakeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.course')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'unique_together': {('student_id', 'course_id')},
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('invitee_name', models.CharField(max_length=200, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class.course')),
                ('invitor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'unique_together': {('invitor_id', 'course_id', 'email')},
            },
        ),
    ]