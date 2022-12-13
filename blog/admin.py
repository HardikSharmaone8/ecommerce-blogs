from django.contrib import admin
from .models import DatabaseBlog,PublishBlog, Comments, Publish_Comments
# Register your models here.
admin.site.register(DatabaseBlog)
admin.site.register(PublishBlog)
admin.site.register(Comments)
admin.site.register(Publish_Comments)