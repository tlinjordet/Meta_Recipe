# Generated by Django 4.2.1 on 2023-05-15 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0009_alter_process_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='type',
            field=models.CharField(blank=True, choices=[('choices', 'choices'), ('time', 'Time')], max_length=50, null=True),
        ),
    ]
