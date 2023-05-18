# Generated by Django 4.2.1 on 2023-05-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('type', models.CharField(blank=True, choices=[('choices', 'choices'), ('time', 'Time')], max_length=50, null=True)),
                ('options', models.JSONField(null=True)),
            ],
            options={
                'verbose_name': 'Process',
                'db_table': 'processes',
            },
        ),
    ]
