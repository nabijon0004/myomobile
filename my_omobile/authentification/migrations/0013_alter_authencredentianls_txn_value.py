# Generated by Django 3.2 on 2022-11-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0012_alter_authencredentianls_txn_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authencredentianls',
            name='txn_value',
            field=models.IntegerField(default=854081),
        ),
    ]