# Generated by Django 2.2.2 on 2019-06-26 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20190626_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
