# Generated by Django 4.2.7 on 2023-11-23 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0003_rename_edegree_degree_rename_edepartment_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professional_Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('working_process', models.TextField(blank=True, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('resign_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Professional_Experience',
                'verbose_name_plural': 'Professional_Experiences',
            },
        ),
    ]
