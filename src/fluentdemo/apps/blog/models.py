from django.db import models
from django.utils.translation import ugettext_lazy as _
from fluent_blogs.base_models import (
    AbstractTranslatableEntry, AbstractTranslatedFieldsEntry,
    ExcerptTextEntryMixin, ExcerptImageEntryMixin
)


class Post(AbstractTranslatableEntry, ExcerptImageEntryMixin):
    """
    Custom blog entry model with an excerpt text.
    """

    class Meta:
        verbose_name = _("Blog post")
        verbose_name_plural = _("Blog posts")
        ordering = ('-publication_date',)  # This is not inherited


class PostTranslation(AbstractTranslatedFieldsEntry, ExcerptTextEntryMixin):
    """
    The translated fields for the blog entry.
    This model is constructed manually because the base table can be constructed from various mixins.
    """
    master = models.ForeignKey(Post, related_name='translations', editable=False, null=True)
