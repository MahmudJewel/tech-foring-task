from django.contrib import admin
from Blog import models


# Register your models here.
admin.site.register(models.BlogCategory)
admin.site.register(models.BlogSubCategory)
admin.site.register(models.FilterOption)
admin.site.register(models.Tags)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.ReadingList)
# admin.site.register(models.BlogSubscription)
