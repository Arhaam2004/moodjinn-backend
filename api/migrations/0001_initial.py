# Generated by Django 3.2 on 2021-04-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SongMood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood', models.CharField(choices=[('HAPPY', 'HAPPY'), ('SAD', 'SAD'), ('ANGRY', 'ANGRY'), ('SURPRISE', 'SURPRISE'), ('NEUTRAL', 'NEUTRAL')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('artist', models.CharField(blank=True, max_length=150, null=True)),
                ('duration', models.DurationField()),
                ('poster', models.ImageField(upload_to='song_posters')),
                ('mp3_file', models.FileField(upload_to='song_files')),
                ('mood', models.ManyToManyField(related_name='songs', to='api.SongMood')),
            ],
        ),
    ]
