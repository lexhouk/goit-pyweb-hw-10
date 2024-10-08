# Generated by Django 5.1 on 2024-09-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpq_quote', '0005_quote_tags'),
        ('fpq_tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(related_name='quotes', to='fpq_tag.tag'),
        ),
    ]
