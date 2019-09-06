from django.contrib import admin
from .models import user, followers, user_status_updates, hastag, user_status_updates_hastags, user_status_update_comments


class  userAdmin(admin.ModelAdmin):
	list_display = ('id', 'email', 'password','login')
class  hastagAdmin(admin.ModelAdmin):
	list_display = ('id', 'hastag')
class followersAdmin(admin.ModelAdmin):
	list_display = ('followerId', 'followedId')
class  user_status_update_commentsAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'body', 'date')
	list_filter = ('user_id', 'date')
class  user_status_updatesAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'body', 'date','id')
	list_filter = ('user_id','date')

admin.site.register(user, userAdmin)
admin.site.register(hastag, hastagAdmin)
admin.site.register(followers, followersAdmin)
admin.site.register(user_status_update_comments, user_status_update_commentsAdmin)
admin.site.register(user_status_updates, user_status_updatesAdmin)

