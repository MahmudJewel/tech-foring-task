from django.contrib import admin
from Academy import models

# Register your models here.
admin.site.register(models.CourseCategory)
admin.site.register(models.Course)
admin.site.register(models.Section)
admin.site.register(models.Content)
admin.site.register(models.BCSCourse)
admin.site.register(models.BCSSection)
admin.site.register(models.BCSContent)
admin.site.register(models.CoursePurchase)
admin.site.register(models.CoursePackage)
admin.site.register(models.PackageFeatures)
admin.site.register(models.CourseOrder)
admin.site.register(models.SubscriptionTeam)
