# Generated by Django 2.2.2 on 2019-06-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basic_app', '0002_auto_20190626_0404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField(default=True)),
                ('title', models.CharField(max_length=30)),
                ('plot', models.TextField(max_length=360)),
                ('director', models.CharField(max_length=30)),
                ('length', models.CharField(max_length=10)),
                ('released_year', models.IntegerField()),
            ],
        ),
    ]
