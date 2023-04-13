# Generated by Django 4.1 on 2022-09-20 19:59

from django.db import migrations, models
import django.db.models.deletion


def fill_highscores(apps, schema_editor):
    Song = apps.get_model("boogie_api", "Song")
    for song in Song.objects.all():
        highscore = song.scores.filter(is_top=True).order_by("-score", "submission_date").first()
        song.highscore = highscore
        song.save()


class Migration(migrations.Migration):
    dependencies = [
        ("boogie_api", "0007_song_gs_ranked"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="highscore",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="highscore_for",
                to="boogie_api.score",
            ),
        ),
        migrations.RunPython(fill_highscores),
    ]
