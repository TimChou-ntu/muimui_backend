# Generated by Django 3.2.7 on 2022-01-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0004_remove_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carID', models.CharField(max_length=20)),
                ('carType', models.CharField(max_length=20)),
                ('serveTime', models.DateTimeField()),
                ('lastMantainTime', models.DateTimeField()),
                ('remainTime', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('m', 'mantainance'), ('a', 'available'), ('r', 'reserved')], default='m', help_text='Car availability', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uID', models.CharField(max_length=20)),
                ('carID', models.CharField(max_length=20)),
                ('startTime', models.DateTimeField()),
                ('duration', models.DurationField()),
            ],
        ),
    ]
