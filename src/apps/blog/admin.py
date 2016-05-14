from django.contrib import admin

from fluent_blogs.admin import EntryAdmin
from .models import Post


@admin.register(Post)
class PostAdmin(EntryAdmin):
    """
    Custom admin for Post model.
    """
    change_form_template = "admin/fluent_blogs/entry/change_form.html"
    change_list_template = "admin/fluent_blogs/entry/change_list.html"
