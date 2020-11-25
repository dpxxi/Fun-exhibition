from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'status']  # Fields displayed in the background of admin
    list_filter = ['name']  
    ordering = ['name']  
    search_fields = ['name']


# The model must be registered in admin.py before it can be displayed on the interface
admin.site.register(User, UserAdmin)
admin.site.register(Artwork)
admin.site.register(Medium)
admin.site.register(OnNowArtwork)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Fabulous)
admin.site.register(Browse)
admin.site.register(HomeSelected)
admin.site.register(Commodity)
admin.site.register(ShoppingCart)
admin.site.register(Order)
admin.site.register(Proposal)
admin.site.register(News)
admin.site.register(Education)
admin.site.register(Remind)
admin.site.register(FabulousComment)
