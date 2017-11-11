from django.contrib import admin
from .models import Album
from .models import Images
from .models import Comments

admin.site.register(Album)
admin.site.register(Images)
admin.site.register(Comments)
