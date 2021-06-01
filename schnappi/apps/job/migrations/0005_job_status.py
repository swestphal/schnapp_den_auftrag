# Generated by Django 3.2.3 on 2021-06-01 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20210601_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('employed', 'employed'), ('archived', 'archived')], default='active', max_length=20),
        ),
    ]
