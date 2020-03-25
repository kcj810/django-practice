from django.contrib import admin
from bookmark.models import Bookmark
# Register your models here.

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')


# 다른 방법
# class BookmarkAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'url')

# admin.site.register(Bookmark, BookmarkAdmin)