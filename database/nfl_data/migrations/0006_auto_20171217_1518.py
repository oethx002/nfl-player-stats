# Generated by Django 2.0 on 2017-12-17 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfl_data', '0005_auto_20171217_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='reveiving_receptions',
            new_name='receiving_receptions',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='reveiving_yards',
            new_name='receiving_yards',
        ),
    ]
