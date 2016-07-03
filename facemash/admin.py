from django.contrib import admin
from .models import photo
# Register your models here.
class photoAdmin(admin.ModelAdmin):
    list_display = ('Name', 'timestamp')
    fieldsets = [
        ('Personal Details',{'fields': ['Name']}),
        ('Upload Image', {'fields': ['image']}),
        ('likes' , {'fields':['nlikes']}),
    ]
    # list_filter = ('Name',)
admin.site.register(photo,photoAdmin)
