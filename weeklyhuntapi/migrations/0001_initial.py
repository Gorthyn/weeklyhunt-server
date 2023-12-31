# Generated by Django 4.2.2 on 2023-07-14 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicMove',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('harm_slots', models.IntegerField()),
                ('luck_slots', models.IntegerField()),
                ('experience_slots', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ChosenBusinessEnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('harm', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChosenForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('harm', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChosenMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Playbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('luck_special', models.TextField()),
                ('required_move_slots', models.IntegerField()),
                ('optional_move_slots', models.IntegerField()),
                ('total_move_slots', models.IntegerField()),
                ('gear_slots', models.IntegerField()),
                ('luck_slots', models.IntegerField()),
                ('harm_slots', models.IntegerField()),
                ('experience_slots', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charm', models.IntegerField()),
                ('cool', models.IntegerField()),
                ('sharp', models.IntegerField()),
                ('tough', models.IntegerField()),
                ('weird', models.IntegerField()),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.playbook')),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isRequired', models.BooleanField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.playbook')),
            ],
        ),
        migrations.CreateModel(
            name='Improvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('improvement', models.CharField(max_length=200)),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.playbook')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.playbook')),
            ],
        ),
        migrations.CreateModel(
            name='Gear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('harm', models.IntegerField()),
                ('playbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.playbook')),
            ],
        ),
        migrations.CreateModel(
            name='ChosenWeapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formHarm', models.IntegerField()),
                ('businessEndHarm1', models.IntegerField()),
                ('businessEndHarm2', models.IntegerField()),
                ('businessEndHarm3', models.IntegerField()),
                ('businessEnd1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapon_businessEnd1', to='weeklyhuntapi.chosenbusinessend')),
                ('businessEnd2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapon_businessEnd2', to='weeklyhuntapi.chosenbusinessend')),
                ('businessEnd3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weapon_businessEnd3', to='weeklyhuntapi.chosenbusinessend')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.character')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.chosenform')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.chosenmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterMove',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.character')),
                ('move', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.move')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterImprovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.character')),
                ('improvement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.improvement')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characterName', models.CharField(max_length=200)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.character')),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.history')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterGear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.character')),
                ('gear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.gear')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='playbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.playbook'),
        ),
        migrations.AddField(
            model_name='character',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weeklyhuntapi.rating'),
        ),
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
