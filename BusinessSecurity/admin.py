from django.contrib import admin
from BusinessSecurity import models

# Register your models here.


admin.site.register(models.NewsSubscriber)
admin.site.register(models.ServiceCategory)
admin.site.register(models.Service)
admin.site.register(models.SubscriptionServices)
admin.site.register(models.ServiceAssigned)
admin.site.register(models.Tracking)
admin.site.register(models.SubService)

admin.site.register(models.InputFields)
admin.site.register(models.SelectChoice)
admin.site.register(models.SelectChoiceRelation)
admin.site.register(models.SubServiceInput)
admin.site.register(models.UserSubserviceInput)
admin.site.register(models.Order)
admin.site.register(models.Quotation)
admin.site.register(models.QuotationAgreement)
admin.site.register(models.SubscriptionOrder)
admin.site.register(models.SubscriptionTeam)


# admin.site.register(models.OrderPrice)

class OrderPriceCustom(admin.ModelAdmin):
    readonly_fields = ['price']


admin.site.register(models.OrderPrice, OrderPriceCustom)

admin.site.register(models.OrderStaff)

admin.site.register(models.SubscriptionBasedPackage)
admin.site.register(models.SubscriptionFeatures)
admin.site.register(models.UserAllowed)
admin.site.register(models.Business)
admin.site.register(models.UsersBusiness)
admin.site.register(models.Events)
admin.site.register(models.RegisteredEvents)

admin.site.register(models.Ticket)
admin.site.register(models.TicketStaff)
admin.site.register(models.TicketComment)

admin.site.register(models.Notification)
admin.site.register(models.AdminNotification)

"""
Subscription Input Sections
Admin will create form for subscription services
Where team member of business can insert their info
"""

admin.site.register(models.SubscriptionField)
admin.site.register(models.SubscriptionInput)
admin.site.register(models.TeamSubscriptionInput)
