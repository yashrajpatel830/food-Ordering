# Generated by Django 5.1.1 on 2024-12-02 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_student_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectMaks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentmaks', to='vege.subject')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vege.subject')),
            ],
            options={
                'unique_together': {('student', 'subject')},
            },
        ),
    ]
