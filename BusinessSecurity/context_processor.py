import datetime

from BusinessSecurity import models, forms
from Account import models as accountmodels
from django.db.models import Q


def NotificationCount(request):
    if request.user.is_authenticated:
        try:
            bcs_notifications = models.Notification.objects.filter(
                Q(category_choice='bcs', is_read=False) | Q(
                    category_choice__iexact=request.user.business_user.business.company_name, is_read=False)).order_by(
                '-notification_time')

            notis = []
            fields = [field.name for field in accountmodels.Interest._meta.get_fields() if
                      field.name != 'id' and field.name != 'user']

            for field in fields:
                interests = accountmodels.Interest.objects.filter(user=request.user).values_list(f'{field}', flat=True)
                # print(interests.values(f'{field}')[0].keys())
                # print(interests)
                if interests[0]:
                    for key in interests.values(f'{field}')[0]:
                        # print(f"{key}")
                        notifications = models.Notification.objects.filter(
                            Q(Q(category_choice='pcs', is_read=False) | Q(category_choice=request.user.email, is_read=False) | Q(
                                category_choice=key, is_read=False))).order_by('-notification_time')
                        # print(notifications)
                        notis.append(notifications)
            new_notifications = []
            all_notifications = []
            for notification in notis:
                for notific in notification:
                    if notific.notification_time.date() == datetime.datetime.today().date():
                        if notific not in new_notifications:
                            new_notifications.append(notific)
                    elif notific.notification_time.date() != datetime.datetime.today().date():
                        if notific.notification_time.date() < datetime.datetime.today().date():
                            if notific not in all_notifications:
                                all_notifications.append(notific)
            bcs_admin_notification = models.AdminNotification.objects.filter(category_choice='bcs', is_read=False)
            pcs_admin_notification = models.AdminNotification.objects.filter(category_choice='pcs', is_read=False)
            return {
                'bcs_notification': bcs_notifications.count(),
                'pcs_notification': len(all_notifications)+len(new_notifications),
                'bcs_admin_notification': bcs_admin_notification.count(),
                'pcs_admin_notification': pcs_admin_notification.count(),
            }
        except:
            notis = []
            fields = [field.name for field in accountmodels.Interest._meta.get_fields() if
                      field.name != 'id' and field.name != 'user']

            for field in fields:
                interests = accountmodels.Interest.objects.filter(user=request.user).values_list(f'{field}', flat=True)
                # print(interests.values(f'{field}')[0].keys())
                # print(interests)
                if interests[0]:
                    for key in interests.values(f'{field}')[0]:
                        # print(f"{key}")
                        notifications = models.Notification.objects.filter(
                            Q(Q(category_choice='pcs', is_read=False) | Q(category_choice=request.user.email,
                                                                          is_read=False) | Q(
                                category_choice=key, is_read=False))).order_by('-notification_time')
                        # print(notifications)
                        notis.append(notifications)
            new_notifications = []
            all_notifications = []
            for notification in notis:
                for notific in notification:
                    if notific.notification_time.date() == datetime.datetime.today().date():
                        if notific not in new_notifications:
                            new_notifications.append(notific)
                    elif notific.notification_time.date() != datetime.datetime.today().date():
                        if notific.notification_time.date() < datetime.datetime.today().date():
                            if notific not in all_notifications:
                                all_notifications.append(notific)

            return {
                'pcs_notification': len(all_notifications)+len(new_notifications),
            }
    else:
        return {

        }