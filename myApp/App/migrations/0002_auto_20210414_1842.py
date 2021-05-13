# Generated by Django 3.1.7 on 2021-04-14 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='completed',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('todolist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.todolist')),
            ],
        ),
    ]
