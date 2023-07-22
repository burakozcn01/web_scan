# Generated by Django 4.2.3 on 2023-07-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NmapResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=100)),
                ('port', models.IntegerField()),
                ('protocol', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('service', models.CharField(max_length=100)),
            ],
        ),
    ]
