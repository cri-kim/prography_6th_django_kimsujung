# Generated by Django 3.0.3 on 2020-03-04 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_remove_board_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='board_dtm',
        ),
        migrations.AddField(
            model_name='board',
            name='add_dtm',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='board',
            name='mod_dtm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='board_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='board',
            name='board_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
