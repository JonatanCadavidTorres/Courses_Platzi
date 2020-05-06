"""Posts admin classes"""

# Django
from django.contrib import admin

# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""

    list_display = ('id', 'user', 'title', 'photo')
    list_display_links = ('id', 'user')
    list_editable = ('title',)

    search_fields = (
        'user__username',
        'title'
    )

    list_filter = (
        'created',
        'modified'
    )