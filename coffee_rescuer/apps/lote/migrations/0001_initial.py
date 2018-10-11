# Generated by Django 2.1.1 on 2018-10-10 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleLote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etapa_hongo', models.PositiveIntegerField(choices=[(0, 'Etapa 0'), (1, 'Etapa 1'), (2, 'Etapa 2'), (3, 'Etapa 3'), (4, 'Etapa 4')], default=0)),
                ('info_sensores', models.FilePathField(match='.*.json$', path='/home/ljpalaciom/Documentos/pythonProjects/roya_cafe/coffee_rescuer/data', recursive=True, unique=True)),
                ('fotos', models.FilePathField(allow_files=False, allow_folders=True, match='lot.*', path='/home/ljpalaciom/Documentos/pythonProjects/roya_cafe/coffee_rescuer/data', recursive=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('ultimo_estado_hongo', models.PositiveIntegerField(choices=[(0, 'Etapa 0'), (1, 'Etapa 1'), (2, 'Etapa 2'), (3, 'Etapa 3'), (4, 'Etapa 4')], default=0)),
                ('finca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finca.Finca')),
            ],
        ),
        migrations.AddField(
            model_name='detallelote',
            name='lote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lote.Lote'),
        ),
    ]
