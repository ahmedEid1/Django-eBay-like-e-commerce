from django.contrib import admin

from .models import Comment, Bid, Listing, Category

# Register your models here.
admin.site.register(Listing)
admin.site.register(Category)
admin.site.register(Bid)
admin.site.register(Comment)
