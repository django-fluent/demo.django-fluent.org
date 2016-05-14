# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import slug_preview.models
import taggit_autosuggest.managers
import fluent_blogs.base_models
import fluent_contents.extensions
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories_i18n', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enable_comments', models.BooleanField(default=True, verbose_name='Enable comments')),
                ('status', models.CharField(default=b'd', max_length=1, verbose_name='status', db_index=True, choices=[(b'p', 'Published'), (b'd', 'Draft')])),
                ('publication_date', models.DateTimeField(help_text='When the entry should go live, status must be "Published".', null=True, verbose_name='publication date', db_index=True)),
                ('publication_end_date', models.DateTimeField(db_index=True, null=True, verbose_name='publication end date', blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='last modification')),
                ('excerpt_image', fluent_contents.extensions.PluginImageField(max_length=100, verbose_name='Intro image')),
                ('author', models.ForeignKey(verbose_name='author', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='categories_i18n.Category', verbose_name='Categories', blank=True)),
                ('parent_site', models.ForeignKey(default=fluent_blogs.base_models._get_current_site, editable=False, to='sites.Site')),
                ('tags', taggit_autosuggest.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-publication_date',),
            },
        ),
        migrations.CreateModel(
            name='PostTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', slug_preview.models.SlugPreviewField(verbose_name='Slug')),
                ('intro', models.TextField(null=True, verbose_name='Introtext')),
                ('excerpt_text', fluent_contents.extensions.PluginHtmlField(help_text='This is the summary in the list of articles.', verbose_name='Excerpt text')),
                ('meta_keywords', models.CharField(default=b'', help_text='When this field is not filled in, the the tags will be used.', max_length=255, verbose_name='keywords', blank=True)),
                ('meta_description', models.CharField(default=b'', help_text='When this field is not filled in, the contents or intro text will be used.', max_length=255, verbose_name='description', blank=True)),
                ('meta_title', models.CharField(help_text='When this field is not filled in, the menu title text will be used.', max_length=255, null=True, verbose_name='page title', blank=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='blog.Post', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
