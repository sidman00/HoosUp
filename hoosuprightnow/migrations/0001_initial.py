# Generated by Django 2.1.1 on 2019-03-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
            ],
            options={
                'managed': True,
            },
        ),
    ]
