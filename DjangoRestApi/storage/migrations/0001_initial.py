# Generated by Django 3.1.3 on 2020-11-18 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.IntegerField(choices=[(0, 'Document'), (1, 'Image'), (2, 'Video'), (3, 'Link')], default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.IntegerField(choices=[(0, 'Rejected'), (1, 'Approved'), (2, 'Pending')], default=2)),
                ('innopoints', models.IntegerField(default=0)),
                ('link', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('tags', models.ManyToManyField(to='storage.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
