# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 22:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_sys', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'autor(a)'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'livro', 'verbose_name_plural': 'livros'},
        ),
        migrations.AlterModelOptions(
            name='bookitem',
            options={'verbose_name': 'exemplar', 'verbose_name_plural': 'exemplares'},
        ),
        migrations.AlterModelOptions(
            name='historyitem',
            options={'verbose_name': 'empréstimo', 'verbose_name_plural': 'empréstimos'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'editora'},
        ),
        migrations.AlterModelOptions(
            name='reader',
            options={'verbose_name': 'usuári@'},
        ),
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.TextField(blank=True, null=True, verbose_name='resenha'),
        ),
        migrations.AddField(
            model_name='book',
            name='synopsis',
            field=models.TextField(blank=True, null=True, verbose_name='sinopse'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, verbose_name='autor(a)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='activated',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_sys.Author', verbose_name='autor(a)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=True, verbose_name='disponível'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, to='library_sys.Category', verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(blank=True, null=True, verbose_name='publicação'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_sys.Publisher', verbose_name='editora'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=100, verbose_name='título'),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_sys.Book', verbose_name='livro'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=160, verbose_name='categoria'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='book_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_sys.BookItem', verbose_name='exemplar'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='daily_fine',
            field=models.SmallIntegerField(default=0, verbose_name='multa diária'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='date_due',
            field=models.DateField(verbose_name='à ser entregue em'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='date_returned',
            field=models.DateField(blank=True, null=True, verbose_name='entregue em'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='date_taken',
            field=models.DateField(verbose_name='emprestado em'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='fine',
            field=models.SmallIntegerField(default=0, verbose_name='multa total'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='is_fine_paid',
            field=models.NullBooleanField(default=False, verbose_name='multa paga?'),
        ),
        migrations.AlterField(
            model_name='historyitem',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_sys.Reader', verbose_name='leitor(a)'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=200, verbose_name='editora'),
        ),
    ]
