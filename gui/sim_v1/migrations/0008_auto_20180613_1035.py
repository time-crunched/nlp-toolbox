# Generated by Django 2.0.5 on 2018-06-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim_v1', '0007_auto_20180608_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='directory',
            field=models.CharField(choices=[('corpus_1', '/Users/Erik/Documents/Utdanning'), ('corpus_2', '/Users/Erik/Documents/Jobb'), ('corpus_3', '/Users/Erik/Dropbox/TekniskBibliotek')], default='/Users/Erik/Documents/Python/NLP/Extraction/Corpus/corpus.mm', max_length=200),
        ),
    ]
