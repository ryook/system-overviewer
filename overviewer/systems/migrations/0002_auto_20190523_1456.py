# Generated by Django 2.2.1 on 2019-05-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='connect_from',
            field=models.ManyToManyField(blank=True, related_name='_system_connect_from_+', to='systems.System', verbose_name='接続元'),
        ),
        migrations.AlterField(
            model_name='system',
            name='connect_to',
            field=models.ManyToManyField(blank=True, related_name='_system_connect_to_+', to='systems.System', verbose_name='接続先'),
        ),
        migrations.AlterField(
            model_name='system',
            name='parent_id',
            field=models.ManyToManyField(blank=True, related_name='_system_parent_id_+', to='systems.System', verbose_name='親システム'),
        ),
    ]
