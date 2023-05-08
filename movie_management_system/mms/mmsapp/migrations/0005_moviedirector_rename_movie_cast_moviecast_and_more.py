# Generated by Django 4.2 on 2023-04-30 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mmsapp', '0004_alter_movie_genre_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moviedirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mmsapp.user')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mmsapp.movie')),
            ],
        ),
        migrations.RenameModel(
            old_name='movie_cast',
            new_name='Moviecast',
        ),
        migrations.RenameModel(
            old_name='movie_genre',
            new_name='Moviegenre',
        ),
        migrations.DeleteModel(
            name='movie_director',
        ),
    ]