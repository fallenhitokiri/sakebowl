# Generated by Django 2.0.6 on 2018-06-21 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0002_entity_configuration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entity',
            old_name='createdAt',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='publishedAt',
            new_name='published_at',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='updatedAt',
            new_name='updated_at',
        ),
    ]