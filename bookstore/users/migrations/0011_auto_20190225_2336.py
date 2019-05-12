# Generated by Django 2.1.5 on 2019-02-25 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20190216_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressinfo',
            name='address',
        ),
        migrations.RemoveField(
            model_name='addressinfo',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Address',
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AddressInfo',
        ),
    ]
