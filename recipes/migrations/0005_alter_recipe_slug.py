# Generated by Django 4.1.7 on 2023-03-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0004_alter_category_name_alter_recipe_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
    ]
