# Generated by Django 4.1.7 on 2023-03-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tag", "0002_remove_tag_content_type_remove_tag_object_id"),
        ("recipes", "0009_recipe_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="tags",
            field=models.ManyToManyField(blank=True, null=True, to="tag.tag"),
        ),
    ]
