# Generated by Django 2.2.1 on 2019-05-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0002_auto_20190523_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='system',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='system',
            name='parent',
            field=models.ManyToManyField(blank=True, related_name='_system_parent_+', to='systems.System', verbose_name='親システム'),
        ),
    ]
