# Generated by Django 4.2.13 on 2024-07-02 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afiha', '0004_event_alter_posts_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-event_time'], 'verbose_name': 'Расписание представлений', 'verbose_name_plural': 'Расписание представлений'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name': 'Доступное представление', 'verbose_name_plural': 'Список доступных представлений'},
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.DateTimeField(verbose_name='Дата и время представления'),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_published',
            field=models.BooleanField(choices=[(False, 'Законченно'), (True, 'Опубликовано')], default=1, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='event',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='afiha.posts', verbose_name='Название представления'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='url_img',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='Картинка'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['-event_time'], name='afiha_event_event_t_2c82ee_idx'),
        ),
    ]