# Generated by Django 2.2.10 on 2020-02-16 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField()),
                ('notification_date', models.DateTimeField()),
                ('expected_end_date', models.DateTimeField(blank=True, null=True)),
                ('complet_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'Done')], default=1)),
                ('color', models.IntegerField(choices=[(1, 'blue'), (2, 'green'), (3, 'red'), (4, 'grey'), (5, 'yellow'), (6, 'white'), (7, 'black')], default=1)),
                ('author', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
