# Generated by Django 4.2.3 on 2023-08-02 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0002_remove_participante_curso_alter_participante_sexo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]
