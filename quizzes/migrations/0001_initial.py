# Generated by Django 3.0 on 2023-05-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('options', models.TextField()),
                ('right_answer', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('inactive', 'Inactive'), ('active', 'Active'), ('finished', 'Finished')], default='inactive', max_length=10)),
            ],
        ),
    ]