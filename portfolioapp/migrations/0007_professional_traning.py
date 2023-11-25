# Generated by Django 4.2.7 on 2023-11-25 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0006_professional_experience_work_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional_Traning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=200, null=True)),
                ('course_duration', models.IntegerField(blank=True, null=True)),
                ('course_institute', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Professional_Traning',
                'verbose_name_plural': 'Professional_Tranings',
            },
        ),
    ]