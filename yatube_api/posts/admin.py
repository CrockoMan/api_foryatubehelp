from django.contrib import admin

from posts.models import Comment, Group, Post

admin.site.register(Group)
admin.site.register(Post)
admin.site.register(Comment)

