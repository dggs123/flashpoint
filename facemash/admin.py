from django.contrib import admin
from .models import photo,total_likes
# Register your models here.
class photoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Details',{'fields': ['Name']}),
        (None, {'fields': ['email']}),
        ('Upload Image', {'fields': ['image']}),
        ('DISCRIPTION/OPTIONAL', {'fields': ['Discription']}),

    ]
admin.site.register(photo,photoAdmin)
admin.site.register(total_likes)
