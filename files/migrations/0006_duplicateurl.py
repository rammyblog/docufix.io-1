# Generated by Django 2.2.6 on 2019-11-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20191023_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='duplicateURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url1', models.URLField()),
            ],
        ),
    ]