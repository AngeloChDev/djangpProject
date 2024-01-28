# Generated by Django 5.0.1 on 2024-01-18 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_date', models.DateField()),
                ('score', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(max_length=50)),
                ('old_teams', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('nationality', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gols_Scored',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minute', models.IntegerField()),
                ('game_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.games', verbose_name='games')),
                ('player_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.players', verbose_name='players')),
            ],
        ),
        migrations.AddField(
            model_name='players',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.profiles', verbose_name='profiles'),
        ),
        migrations.AddField(
            model_name='players',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.teams', verbose_name='teams'),
        ),
        migrations.AddField(
            model_name='games',
            name='opponent',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='team.teams'),
        ),
    ]
