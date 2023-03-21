# Generated by Django 3.0.7 on 2020-07-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_remove_ingredientofrecipe_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientofrecipe',
            name='ketogenic_value',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='ingredientofrecipe',
            name='kosher_value',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='ingredientofrecipe',
            name='vegan_value',
            field=models.FloatField(default=0.0),
        ),
    ]