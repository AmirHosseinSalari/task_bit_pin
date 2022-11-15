# Generated by Django 4.0.6 on 2022-11-15 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('score', models.IntegerField()),
                ('content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='content.content')),
            ],
        ),
    ]
