# Generated by Django 4.1.7 on 2023-02-21 10:35

from django.db import migrations, models
import django.db.models.deletion
import fileuploader.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=fileuploader.models.get_upload_path)),
                ('created_at', models.DateField(auto_now=True)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileuploader.folder')),
            ],
        ),
    ]
