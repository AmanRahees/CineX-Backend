# Generated by Django 4.2.5 on 2023-10-07 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_alter_movie_ratings"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banners",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("banner", models.ImageField(upload_to="banners/")),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.movie"
                    ),
                ),
            ],
        ),
    ]
