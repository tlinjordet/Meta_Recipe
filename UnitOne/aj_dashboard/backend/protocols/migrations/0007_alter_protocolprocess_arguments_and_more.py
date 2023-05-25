# Generated by Django 4.2.1 on 2023-05-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocols', '0006_protocol_created_at_protocol_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolprocess',
            name='arguments',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='protocolprocess',
            name='duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='protocolprocess',
            name='duration_type',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='protocolprocess',
            name='input_ingredients',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='protocolprocess',
            name='output_ingredients',
            field=models.JSONField(null=True),
        ),
    ]
