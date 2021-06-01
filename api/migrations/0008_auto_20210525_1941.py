# Generated by Django 3.2 on 2021-05-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_user_mood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='_api_user_followers_+', to='api.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mood',
            field=models.CharField(blank=True, choices=[('Happy', 'Happy'), ('Sad', 'Sad'), ('Angry', 'Angry'), ('Surprised', 'Surprised'), ('Neutral', 'Neutral')], max_length=150, null=True),
        ),
    ]
