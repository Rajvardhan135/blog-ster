# Generated by Django 5.0.3 on 2024-03-10 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_managers_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
