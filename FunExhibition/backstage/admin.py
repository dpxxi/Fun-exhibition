from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'status']  # admin后台展示的字段
    list_filter = ['name']  # 后边查询
    ordering = ['name']  # 排序
    search_fields = ['name']


# model必须在admin.py中注册后才能在界面上显示
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
