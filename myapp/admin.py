from django.contrib import admin
from .models import bloglab
# Register your models here.
@admin.register(bloglab)
class usermodeladmin(admin.ModelAdmin):
    list_display=['title','updated_on','content','created_on','photo']
