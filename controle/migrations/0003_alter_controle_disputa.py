# Generated by Django 4.1.7 on 2023-03-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_alter_controle_options_alter_controle_proc_ele'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='disputa',
            field=models.CharField(choices=[('MP', 'Menor preço'), ('TP', 'Técnica e Preço')], max_length=2),
        ),
    ]
