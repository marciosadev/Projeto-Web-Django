# Generated by Django 4.1.7 on 2023-03-03 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='controle',
            options={'verbose_name': 'Controle TES'},
        ),
        migrations.AlterField(
            model_name='controle',
            name='proc_ele',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1),
        ),
    ]