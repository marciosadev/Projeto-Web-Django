# Generated by Django 4.1.7 on 2023-03-03 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0024_alter_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 3, 10, 7, 7, 306451)),
        ),
    ]