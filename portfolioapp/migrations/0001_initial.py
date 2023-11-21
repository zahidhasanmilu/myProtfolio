# Generated by Django 4.2.7 on 2023-11-20 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('profile_pic', models.ImageField(upload_to='Uploaded/Profile_pic/')),
                ('short_description', models.TextField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('linkdin', models.URLField(blank=True, null=True)),
                ('age', models.CharField(blank=True, max_length=3, null=True)),
                ('degree', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('freelance_status', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Aboutme',
                'verbose_name_plural': 'Aboutmes',
            },
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_count', models.CharField(blank=True, max_length=100, null=True)),
                ('count_number', models.IntegerField(blank=True, null=True)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Count',
                'verbose_name_plural': 'Counts',
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('icon', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Interest',
                'verbose_name_plural': 'Interests',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('progress', models.IntegerField(default=10)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
    ]
