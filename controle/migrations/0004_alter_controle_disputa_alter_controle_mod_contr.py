# Generated by Django 4.1.7 on 2023-03-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0003_alter_controle_disputa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='disputa',
            field=models.CharField(choices=[('A', 'Aberta'), ('F', 'Fechada')], max_length=1),
        ),
        migrations.AlterField(
            model_name='controle',
            name='mod_contr',
            field=models.CharField(choices=[('MP', 'Menor preço'), ('TP', 'Técnica e Preço')], max_length=2),
        ),
    ]