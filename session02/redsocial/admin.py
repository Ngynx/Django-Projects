from django.contrib import admin
from .models import user
from .models import followers
from .models import hastag
from .models import user_status_updates
from .models import user_status_update_comments
admin.site.register(user)
admin.site.register(followers)
admin.site.register(hastag)
admin.site.register(user_status_updates)
admin.site.register(user_status_update_comments)

# Register your models here.
