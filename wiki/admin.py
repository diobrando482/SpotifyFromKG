from django.contrib import admin
from .models import Group, Album, Song, GroupMember

admin.site.register(Group)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(GroupMember)
