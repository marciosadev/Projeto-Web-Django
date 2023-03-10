# Generated by Django 4.1.7 on 2023-03-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0004_alter_controle_disputa_alter_controle_mod_contr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='crit_julg',
            field=models.CharField(choices=[('MP', 'Menor preço'), ('TP', 'Técnica e Preço')], max_length=2),
        ),
        migrations.AlterField(
            model_name='controle',
            name='mod_contr',
            field=models.CharField(choices=[('LI', 'Licitação Sabesp'), ('PG', 'Pregão'), ('DV', 'Dispensa'), ('CV', 'Convite')], max_length=2),
        ),
    ]
