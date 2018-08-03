# Generated by Django 2.0.6 on 2018-08-03 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('Album_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Album_Title', models.CharField(blank=True, max_length=140, null=True)),
                ('Release_Date', models.DateField()),
                ('Album_Length', models.DurationField(blank=True, null=True)),
                ('Album_Label', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('Artist_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Artist_Name', models.CharField(max_length=140)),
                ('Year_Established', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('Genre_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Genre_Name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('Song_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Song_Title', models.CharField(max_length=140)),
                ('Song_Length', models.DurationField(blank=True, null=True)),
                ('Release_Date', models.DateField()),
                ('Album_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Album')),
                ('Artist_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Artist')),
                ('Genre_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Genre')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='Artist_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='Genre_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Genre'),
        ),
    ]
