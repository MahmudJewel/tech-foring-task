# Generated by Django 3.2.7 on 2021-12-28 07:11

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(choices=[('Business', 'Business'), ('Personal', 'Personal')], max_length=264)),
                ('course_name', models.CharField(max_length=264)),
                ('duration', models.CharField(choices=[('one_month', 'One Month'), ('two_months', 'Two Months'), ('three_months', 'Three Months'), ('six_months', 'Six Months'), ('one_year', 'One Year')], max_length=264)),
                ('short_description', models.TextField(max_length=1000)),
                ('long_description', tinymce.models.HTMLField(max_length=5000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_type', models.CharField(choices=[('Business', 'Business'), ('Personal', 'Personal')], max_length=264)),
                ('category_name', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=264)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_course', to='Academy.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_coursecategory', to='Academy.coursecategory'),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_name', models.CharField(max_length=264)),
                ('text_instruction', models.FileField(upload_to='course/')),
                ('course_video', models.FileField(upload_to='course/')),
                ('preview_video', models.FileField(blank=True, null=True, upload_to='course/')),
                ('resource_file', models.FileField(upload_to='course/')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_section', to='Academy.section')),
            ],
        ),
    ]
