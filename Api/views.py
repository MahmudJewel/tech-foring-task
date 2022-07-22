import base64
import calendar
import itertools

import requests
from django.conf import settings
from django.shortcuts import render
from Api import serializer
from rest_framework import generics
from Blog import models
from Account import models as accountmodel
from BusinessSecurity import models as bcsmodels
from Academy import models as coursemodels
from rest_framework import permissions, pagination, filters
from datetime import date
from django.db.models import Q
from rest_framework.response import Response
from Api import apipermissions
from django.utils import timezone
from datetime import date, timedelta
from rest_framework import status

# Create your views here.

class PostApi(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializer.PostSerializer


class CategoryApi(generics.ListAPIView):
    permission_classes = [apipermissions.IsBlogAdmin]
    queryset = models.BlogCategory.objects.all()
    serializer_class = serializer.CategorySerializer


class SubCategoryApi(generics.ListAPIView):
    # queryset = models.BlogSubCategory.objects.all()
    permission_classes = [apipermissions.IsBlogAdmin]
    serializer_class = serializer.SubCategorySerializer

    def get_queryset(self):
        category = self.kwargs['id']
        return models.BlogSubCategory.objects.filter(category=category)


class FilterApi(generics.ListAPIView):
    # queryset = models.FilterOption.objects.all()
    permission_classes = [apipermissions.IsBlogAdmin]
    serializer_class = serializer.FilterSerializer

    def get_queryset(self):
        category = self.kwargs['id']
        subcategory = self.kwargs['sub_id']
        return models.FilterOption.objects.filter(sub_category=subcategory, sub_category__category=category)


class Page(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 5


class AllCommentCreateViewApi(generics.ListCreateAPIView):
    serializer_class = serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Page
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['comment_date']


class CommentCreateViewApi(generics.ListCreateAPIView):
    serializer_class = serializer.CommentSerializer
    queryset = models.Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = Page

    def get_queryset(self):
        post = self.kwargs['post_id']
        return models.Comment.objects.filter(post=post)


class BlogFilterApiView(generics.ListAPIView):
    serializer_class = serializer.BlogFilterSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        text = self.kwargs['text']
        return models.Post.objects.filter(
            Q(category__category__iexact=category, title__icontains=text) | Q(category__category__iexact=category,
                                                                              short_description__icontains=text))


class BlogFilterDateApiView(generics.ListAPIView):
    serializer_class = serializer.BlogFilterSerializer
    today = date.today()

    def get_queryset(self):
        category = self.kwargs['category']
        text = self.kwargs['text']
        if text == 'month':
            return models.Post.objects.filter(category__category__iexact=category, date__month=self.today.month)
        elif text == 'year':
            return models.Post.objects.filter(category__category__iexact=category, date__year=self.today.year)


class PackageListViewApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializer.PackageListSerializer

    # queryset = bcsmodels.SubscriptionBasedPackage.objects.all()

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubscriptionBasedPackage.objects.filter(service_id=service_id)


class SubscriptionServiceApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializer.SubscriptionServiceSerializer
    lookup_field = 'id'

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubscriptionServices.objects.filter(id=service_id)


class ServiceListApiView(generics.ListAPIView):
    serializer_class = serializer.ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    # queryset = bcsmodels.Service.objects.all()

    def get_queryset(self):
        cat_type = self.kwargs['cat']
        return bcsmodels.Service.objects.filter(category_choice=cat_type)


class SubServiceApiView(generics.ListAPIView):
    serializer_class = serializer.SubServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubService.objects.filter(service_id=service_id)


class SubServiceInputApiView(generics.ListAPIView):
    serializer_class = serializer.SubServiceInputSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubServiceInput.objects.filter(subservice_id=service_id)


class SubscriptionInputApiView(generics.ListAPIView):
    serializer_class = serializer.SubscriptionInputSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        service_id = self.kwargs['id']
        return bcsmodels.SubscriptionInput.objects.filter(subscription_field_id=service_id)


class ChoiceApiView(generics.ListAPIView):
    serializer_class = serializer.ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        id = self.kwargs['id']
        return bcsmodels.SelectChoiceRelation.objects.filter(input_field_id=id)


class UserSubServiceOrderApiView(generics.ListAPIView):
    serializer_class = serializer.UserSubServiceOrderSerializer

    def get_queryset(self):
        subservice_id = self.kwargs['id']
        return bcsmodels.Order.objects.filter(id=subservice_id)


class TeamPermissionApiView(generics.RetrieveUpdateAPIView):
    serializer_class = serializer.TeamPermissionSerializer
    permission_classes = [apipermissions.IsTeamAdmin]
    lookup_field = 'id'
    queryset = bcsmodels.UsersBusiness


class BCSAdminDashboardAllChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()
    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        # responseData = ser.data

        start_date = 2014
        end_date = date.today().year
        all_years = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []

        query = bcsmodels.Order.objects.filter(category_choice='bcs')
        subscriptions = bcsmodels.SubscriptionOrder.objects.filter(subscription_service__category_choice='bcs')

        for year in all_years:
            order = query.filter(order_date__year=year).count()
            unsubscription_count.append(order)
        for year in all_years:
            order = subscriptions.filter(create_time__year=year).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        # responseData.append({
        #     'x_axis': all_years,
        #     'datas': datas
        # })
        return Response({
            'x_axis': all_years,
            'datas': datas
        })


class BCSAdminDashboardYearChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()

    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        # responseData = ser.data

        start_date = 1
        end_date = date.today().month
        all_months = list(range(start_date, end_date + 1))
        # print(all_months)
        current_year = date.today().year

        subscription_count = []
        unsubscription_count = []

        query = bcsmodels.Order.objects.filter(category_choice='bcs')
        subscriptions = bcsmodels.SubscriptionOrder.objects.filter(subscription_service__category_choice='bcs')

        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year).count()
            unsubscription_count.append(order)
        for month in all_months:
            order = subscriptions.filter(create_time__month=month, create_time__year=current_year).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        # responseData.append({
        #     'x_axis': all_months,
        #     'datas': datas
        # })
        months = []
        for month in all_months:
            months.append(calendar.month_name[month])
        return Response({
            'x_axis': months,
            'datas': datas
        })
class BCSAdminDashboardRangeChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()

    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        s_month=int(start_date.split('-')[1])
        s_year=int(start_date.split('-')[0])
        e_month=int(end_date.split('-')[1])
        e_year=int(end_date.split('-')[0])
        if s_year<=e_year:
            end_date = date.today().month
            all_months = list(range(s_month, e_month+ 1))
            current_year = date.today().year

            subscription_count = []
            unsubscription_count = []

            query = bcsmodels.Order.objects.filter(category_choice='bcs')
            subscriptions = bcsmodels.SubscriptionOrder.objects.filter(subscription_service__category_choice='bcs')
            if e_year>s_year:
                for year in range(s_year,e_year+1):
                    if year==s_year:
                        for month in range(s_month,13):
                            order = query.filter(order_date__month=month,order_date__year=year).count()
                            unsubscription_count.append(order)
                            order = subscriptions.filter(create_time__month=month,create_time__year=year).count()
                            subscription_count.append(order)
                    elif year==e_year:
                        for month in range(1,e_month+1):
                            order = query.filter(order_date__month=month,order_date__year=year).count()
                            unsubscription_count.append(order)
                            order = subscriptions.filter(create_time__month=month,create_time__year=year).count()
                            subscription_count.append(order)
                    else:
                        for month in range(1,13):
                            order = query.filter(order_date__month=month,order_date__year=year).count()
                            unsubscription_count.append(order)
                            order = subscriptions.filter(create_time__month=month,create_time__year=year).count()
                            subscription_count.append(order)
                    # for month in range(s_month,13):
                    #     order = query.filter(order_date__month=month, order_date__year=current_year).count()
                    #     unsubscription_count.append(order)
                    # for month in all_months:
                    #     order = subscriptions.filter(create_time__month=month, create_time__year=current_year).count()
                    #     subscription_count.append(order)
            else:
                current_year=s_year
                for month in range(s_month,e_month+1):
                        order = query.filter(order_date__month=month, order_date__year=current_year).count()
                        unsubscription_count.append(order)
                for month in range(s_month,e_month+1):
                        order = subscriptions.filter(create_time__month=month, create_time__year=current_year).count()
                        subscription_count.append(order)

            total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))
            datas = {
                'for_subscription': subscription_count,
                'for_unsubscription': unsubscription_count,
                'total_count': total_count,
            }

            months = []
            if e_year>s_year:
                for year in range(s_year,e_year+1):
                    if year==s_year:
                        for month in range(s_month,13):
                            months.append((calendar.month_name[month],year))
                    elif year==e_year:
                        for month in range(1,e_month+1):
                            months.append((calendar.month_name[month],year))
                    else:
                        for month in range(1,13):
                            months.append((calendar.month_name[month],year))
            else:
                for month in range(s_month,e_month+1):
                    months.append(calendar.month_name[month])

            return Response({
                'x_axis': months,
                'datas': datas
            })
        else:
            res = {'response': 'Please add valid date'}
            return Response(res ,status=status.HTTP_404_NOT_FOUND)



class BCSAdminDashboardMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()

    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        # responseData = ser.data

        start_date = 1
        end_date = date.today().day
        # print(end_date)
        all_dates = list(range(start_date, end_date + 1))
        # print(all_dates)
        current_month = date.today().month

        subscription_count = []
        unsubscription_count = []

        query = bcsmodels.Order.objects.filter(category_choice='bcs')
        subscriptions = bcsmodels.SubscriptionOrder.objects.filter(subscription_service__category_choice='bcs')

        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = subscriptions.filter(create_time__day=day, create_time__month=current_month).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        # responseData.append({
        #     'x_axis': all_months,
        #     'datas': datas
        # })
        return Response({
            'x_axis': all_dates,
            'datas': datas
        })
class BCSAdminDashboardLastMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # queryset = bcsmodels.Order.objects.all()

    # def get_queryset(self):
    #     w = bcsmodels.Order.objects.filter(service__is_subscription_based=False)
    #     # print(w.values_list())
    #     return bcsmodels.Order.objects.all()

    def list(self, request, *args, **kwargs):
        # ser = self.get_serializer(self.get_queryset(), many=True)
        # responseData = ser.data

        start_date = 1
        end_date = calendar.monthrange(date.today().year, date.today().month - 1)[1]
        # print(end_date)
        all_dates = list(range(start_date, end_date + 1))
        # print(all_dates)
        current_month = (date.today().month) - 1

        subscription_count = []
        unsubscription_count = []

        query = bcsmodels.Order.objects.filter(category_choice='bcs')
        subscriptions = bcsmodels.SubscriptionOrder.objects.filter(subscription_service__category_choice='bcs')

        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = subscriptions.filter(create_time__day=day, create_time__month=current_month).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        # responseData.append({
        #     'x_axis': all_months,
        #     'datas': datas
        # })
        return Response({
            'x_axis': all_dates,
            'datas': datas
        })


class PCSAdminDashboardAllChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):
        start_date = 2014
        end_date = date.today().year
        all_years = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []

        query = bcsmodels.Order.objects.filter(category_choice='pcs')
        subscriptions = bcsmodels.SubscriptionOrder.objects.filter(subscription_service__category_choice='pcs')

        for year in all_years:
            order = query.filter(order_date__year=year).count()
            unsubscription_count.append(order)
        for year in all_years:
            order = subscriptions.filter(create_time__year=year).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_years,
            'datas': datas
        })


class PCSAdminDashboardYearChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().month
        all_months = list(range(start_date, end_date + 1))
        current_year = date.today().year

        subscription_count = []
        unsubscription_count = []

        query = bcsmodels.Order.objects.filter(category_choice='pcs')
        subscriptions = bcsmodels.SubscriptionOrder.objects.filter(subscription_service__category_choice='pcs')

        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year).count()
            unsubscription_count.append(order)
        for month in all_months:
            order = subscriptions.filter(create_time__month=month, create_time__year=current_year).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        months = []
        for month in all_months:
            months.append(calendar.month_name[month])

        return Response({
            'x_axis': months,
            'datas': datas
        })
class PCSAdminDashboardRangeChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        s_month=int(start_date.split('-')[1])
        s_year=int(start_date.split('-')[0])
        e_month=int(end_date.split('-')[1])
        e_year=int(end_date.split('-')[0])
        if s_year<=e_year:
            end_date = date.today().month
            all_months = list(range(s_month, e_month+ 1))
            current_year = date.today().year

            subscription_count = []
            unsubscription_count = []

            query = bcsmodels.Order.objects.filter(category_choice='pcs')
            subscriptions = bcsmodels.SubscriptionOrder.objects.filter(subscription_service__category_choice='pcs')
            if e_year>s_year:
                for year in range(s_year,e_year+1):
                    if year==s_year:
                        for month in range(s_month,13):
                            order = query.filter(order_date__month=month,order_date__year=year).count()
                            unsubscription_count.append(order)
                            order = subscriptions.filter(create_time__month=month,create_time__year=year).count()
                            subscription_count.append(order)
                    elif year==e_year:
                        for month in range(1,e_month+1):
                            order = query.filter(order_date__month=month,order_date__year=year).count()
                            unsubscription_count.append(order)
                            order = subscriptions.filter(create_time__month=month,create_time__year=year).count()
                            subscription_count.append(order)
                    else:
                        for month in range(1,13):
                            order = query.filter(order_date__month=month,order_date__year=year).count()
                            unsubscription_count.append(order)
                            order = subscriptions.filter(create_time__month=month,create_time__year=year).count()
                            subscription_count.append(order)
                    # for month in range(s_month,13):
                    #     order = query.filter(order_date__month=month, order_date__year=current_year).count()
                    #     unsubscription_count.append(order)
                    # for month in all_months:
                    #     order = subscriptions.filter(create_time__month=month, create_time__year=current_year).count()
                    #     subscription_count.append(order)
            else:
                current_year=s_year
                for month in range(s_month,e_month+1):
                        order = query.filter(order_date__month=month, order_date__year=current_year).count()
                        unsubscription_count.append(order)
                for month in range(s_month,e_month+1):
                        order = subscriptions.filter(create_time__month=month, create_time__year=current_year).count()
                        subscription_count.append(order)

            total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))
            datas = {
                'for_subscription': subscription_count,
                'for_unsubscription': unsubscription_count,
                'total_count': total_count,
            }

            months = []
            if e_year>s_year:
                for year in range(s_year,e_year+1):
                    if year==s_year:
                        for month in range(s_month,13):
                            months.append((calendar.month_name[month],year))
                    elif year==e_year:
                        for month in range(1,e_month+1):
                            months.append((calendar.month_name[month],year))
                    else:
                        for month in range(1,13):
                            months.append((calendar.month_name[month],year))
            else:
                for month in range(s_month,e_month+1):
                    months.append(calendar.month_name[month])

            return Response({
                'x_axis': months,
                'datas': datas
            })
        else:
            res = {'response': 'Please add valid date'}
            return Response(res ,status=status.HTTP_404_NOT_FOUND)


class PCSAdminDashboardMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().day

        all_dates = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []

        current_month = date.today().month

        query = bcsmodels.Order.objects.filter(category_choice='pcs')
        subscriptions = bcsmodels.SubscriptionOrder.objects.filter(subscription_service__category_choice='pcs')

        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = subscriptions.filter(create_time__day=day, create_time__month=current_month).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_dates,
            'datas': datas
        })
class PCSAdminDashboardLastMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsPCSAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = calendar.monthrange(date.today().year, date.today().month - 1)[1]

        all_dates = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []

        current_month = (date.today().month)-1

        query = bcsmodels.Order.objects.filter(category_choice='pcs')
        subscriptions = bcsmodels.SubscriptionOrder.objects.filter(subscription_service__category_choice='pcs')

        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = subscriptions.filter(create_time__day=day, create_time__month=current_month).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_dates,
            'datas': datas
        })


class MainAdminDashboardAllChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):
        start_date = 2014
        end_date = date.today().year
        all_years = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []

        query = bcsmodels.Order.objects.all()
        subscriptions = bcsmodels.SubscriptionOrder.objects.all()

        for year in all_years:
            order = query.filter(order_date__year=year).count()
            unsubscription_count.append(order)
        for year in all_years:
            order = subscriptions.filter(create_time__year=year).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_years,
            'datas': datas
        })


class MainAdminDashboardRangeChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        print(start_date, end_date)
        s_month=int(start_date.split('-')[1])
        s_year=int(start_date.split('-')[0])
        e_month=int(end_date.split('-')[1])
        e_year=int(end_date.split('-')[0])
        if s_year<=e_year:
            print("ok")
            end_date = date.today().month
            all_months = list(range(s_month, e_month+ 1))
            current_year = date.today().year

            subscription_count = []
            unsubscription_count = []

            query = bcsmodels.Order.objects.all()
            subscriptions = bcsmodels.SubscriptionOrder.objects.all()
            if e_year>s_year:
                for year in range(s_year,e_year+1):
                    if year==s_year:
                        for month in range(s_month,13):
                            order = query.filter(order_date__month=month,order_date__year=year).count()
                            unsubscription_count.append(order)
                            order = subscriptions.filter(create_time__month=month,create_time__year=year).count()
                            subscription_count.append(order)
                    elif year==e_year:
                        for month in range(1,e_month+1):
                            order = query.filter(order_date__month=month,order_date__year=year).count()
                            unsubscription_count.append(order)
                            order = subscriptions.filter(create_time__month=month,create_time__year=year).count()
                            subscription_count.append(order)
                    else:
                        for month in range(1,13):
                            order = query.filter(order_date__month=month,order_date__year=year).count()
                            unsubscription_count.append(order)
                            order = subscriptions.filter(create_time__month=month,create_time__year=year).count()
                            subscription_count.append(order)
                    # for month in range(s_month,13):
                    #     order = query.filter(order_date__month=month, order_date__year=current_year).count()
                    #     unsubscription_count.append(order)
                    # for month in all_months:
                    #     order = subscriptions.filter(create_time__month=month, create_time__year=current_year).count()
                    #     subscription_count.append(order)
            else:
                current_year=s_year
                
                for month in range(s_month,e_month+1):
                        order = query.filter(order_date__month=month, order_date__year=current_year).count()
                        unsubscription_count.append(order)
                for month in range(s_month,e_month+1):
                        order = subscriptions.filter(create_time__month=month, create_time__year=current_year).count()
                        subscription_count.append(order)

            total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))
            datas = {
                'for_subscription': subscription_count,
                'for_unsubscription': unsubscription_count,
                'total_count': total_count,
            }

            months = []
            if e_year>s_year:
                for year in range(s_year,e_year+1):
                    if year==s_year:
                        for month in range(s_month,13):
                            months.append((calendar.month_name[month],year))
                    elif year==e_year:
                        for month in range(1,e_month+1):
                            months.append((calendar.month_name[month],year))
                    else:
                        for month in range(1,13):
                            months.append((calendar.month_name[month],year))
            else:
                for month in range(s_month,e_month+1):
                    months.append(calendar.month_name[month])

            return Response({
                'x_axis': months,
                'datas': datas
            })
        else:
            res = {'response': 'Please add valid date'}
            return Response(res ,status=status.HTTP_404_NOT_FOUND)
class MainAdminDashboardYearChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):
        #total months between 2014 and current year
        start_date = 1
        end_date = date.today().month
        all_months = list(range(start_date, end_date + 1))
        current_year = date.today().year

        subscription_count = []
        unsubscription_count = []

        query = bcsmodels.Order.objects.all()
        subscriptions = bcsmodels.SubscriptionOrder.objects.all()
        print(all_months)
        for month in all_months:
            order = query.filter(order_date__month=month, order_date__year=current_year).count()
            unsubscription_count.append(order)
        for month in all_months:
            order = subscriptions.filter(create_time__month=month, create_time__year=current_year).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        months = []
        for month in all_months:
            months.append(calendar.month_name[month])
        return Response({
            'x_axis': months,
            'datas': datas
        })


class MainAdminDashboardMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        end_date = date.today().day

        all_dates = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []

        current_month = date.today().month

        query = bcsmodels.Order.objects.all()
        subscriptions = bcsmodels.SubscriptionOrder.objects.all()

        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = subscriptions.filter(create_time__day=day, create_time__month=current_month).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_dates,
            'datas': datas
        })

class MainAdminDashboardLastMonthChartApiView(generics.ListAPIView):
    serializer_class = serializer.BCSAdminDashboardChartSerializer
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):

        start_date = 1
        #get last month total day
        end_date = calendar.monthrange(date.today().year, date.today().month - 1)[1]
        all_dates = list(range(start_date, end_date + 1))

        subscription_count = []
        unsubscription_count = []

        current_month = (date.today().month) - 1
        query = bcsmodels.Order.objects.all()
        subscriptions = bcsmodels.SubscriptionOrder.objects.all()

        for day in all_dates:
            order = query.filter(order_date__day=day, order_date__month=current_month).count()
            unsubscription_count.append(order)
        for day in all_dates:
            order = subscriptions.filter(create_time__day=day, create_time__month=current_month).count()
            subscription_count.append(order)

        total_count = (sum(x) for x in zip(unsubscription_count, subscription_count))

        datas = {
            'for_subscription': subscription_count,
            'for_unsubscription': unsubscription_count,
            'total_count': total_count,
        }

        return Response({
            'x_axis': all_dates,
            'datas': datas
        })


class SubscriptionApiView(generics.ListAPIView):
    serializer_class = serializer.SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'service'

    def get_queryset(self):
        service_id = self.kwargs['service']
        return bcsmodels.Order.objects.filter(service__id=service_id, user=self.request.user,
                                              service__is_subscription_based=True).order_by('-order_date')

    # def list(self, request, *args, **kwargs):
    #     ser = self.get_serializer(self.get_queryset(), many=True)
    #     responseData = ser.data
    #     print(self.get_queryset())
    #     responseData.append({
    #         'price': '1223'
    #     })
    #     return Response(responseData)


class SubscriptionOrderView(generics.CreateAPIView):
    serializer_class = serializer.SubscriptionOrderSerializer
    queryset = bcsmodels.SubscriptionOrder
    permission_classes = [permissions.IsAuthenticated]

    def cancelSubscriptions(self, subscription_service, category_choice):
        """
        Cancelling Previous Subscriptions
        """
        username = settings.PAYPAL_USER
        password = settings.PAYPAL_PASS
        busername = str(base64.b64encode(bytes(username, 'utf-8')))[1:].replace("'", "").replace("=", '')
        bpassword = str(base64.b64encode(bytes(password, 'utf-8')))[1:].replace("'", "")
        bearer = f"Basic {busername}6{bpassword}"

        packages = bcsmodels.SubscriptionBasedPackage.objects.filter(
            service_id__category_choice=category_choice).values_list(
            'id')
        if category_choice == 'pcs':
            user_orders = bcsmodels.SubscriptionOrder.objects.filter(
                # user__business_user__business=self.request.user.business_user.business,
                user=self.request.user,
                subscription_package__in=packages,
                subscription_service=subscription_service,
                is_active=True
            )
            for current_order in user_orders:
                current_order.is_active = False
                current_order.save()
                url = f'{settings.PAYPAL_URL}billing/subscriptions/{current_order.paypal_subscription_id}/cancel'
                headers = {
                    'Content-type': 'application/json',
                    'Authorization': bearer
                }
                r = requests.post(url, headers=headers)
                print(r.status_code)
                # current_business = bcsmodels.Business.objects.get(business_business__user=self.request.user)
                # order_subscription_teams = bcsmodels.SubscriptionTeam.objects.filter(business=current_business,
                #                                                                      subscription_order=current_order)
                # if order_subscription_teams.exists():
                #     for team in order_subscription_teams:
                #         team.delete()
            if user_orders.exists():
                notification = bcsmodels.AdminNotification.objects.create(category_choice='pcs',
                                                                          user=self.request.user,
                                                                          notification=f'User has cancelled the '
                                                                                       f'subs'
                                                                                       f'cription for '
                                                                                       f'{current_order.subscription_service.service_title}')
                notification.save()

        elif category_choice == 'bcs':
            user_orders = bcsmodels.SubscriptionOrder.objects.filter(
                user__business_user__business=self.request.user.business_user.business,
                # user=self.request.user,
                subscription_package__in=packages,
                subscription_service=subscription_service,
                is_active=True
            )
            for current_order in user_orders:
                current_order.is_active = False
                current_order.save()
                url = f'{settings.PAYPAL_URL}billing/subscriptions/{current_order.paypal_subscription_id}/cancel'
                headers = {
                    'Content-type': 'application/json',
                    'Authorization': bearer
                }
                r = requests.post(url, headers=headers)
                print(r.status_code)
            if user_orders.exists():
                notification = bcsmodels.AdminNotification.objects.create(category_choice='bcs',
                                                                          business=self.request.user.business_user.business,
                                                                          notification=f'User has cancelled the '
                                                                                       f'subs'
                                                                                       f'cription for '
                                                                                       f'{current_order.subscription_service.service_title}')
                notification.save()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, is_active=True)

    def create(self, request, *args, **kwargs):
        subscription_service = request.data['subscription_service']
        subscription_package = request.data['subscription_package']
        category_choice = request.data['category_choice']
        if category_choice == 'pcs':
            try:
                check_existing_order = bcsmodels.SubscriptionOrder.objects.get(user=self.request.user,
                                                                               subscription_service=subscription_service,
                                                                               subscription_package=subscription_package,
                                                                               is_active=True)
                return Response({'response': 'You have already Subscribed to this Package'})
            except:
                self.cancelSubscriptions(subscription_service, 'pcs')
                """
                Creating new Subscription
                """
                ser = self.get_serializer(data=request.data)
                ser.is_valid(raise_exception=True)
                self.perform_create(ser)
                subscription_id = request.data['paypal_subscription_id']
                user_subscribed = bcsmodels.SubscriptionOrder.objects.get(paypal_subscription_id=subscription_id)

                notification = bcsmodels.AdminNotification.objects.create(category_choice='pcs',
                                                                          user=self.request.user,
                                                                          notification=f'New Subscription. '
                                                                                       f'<div><a href="https://pcs.techforing.com/pcs_admin_subscription_detail/{user_subscribed.id}/" target="_blank" class="btn btn-success mt-2">Visit Now</a></div>')
                notification.save()
                return Response(ser.data)
        elif category_choice == 'bcs':
            try:
                check_existing_order = bcsmodels.SubscriptionOrder.objects.get(
                    user__business_user__business=self.request.user.business_user.business,
                    subscription_service=subscription_service,
                    subscription_package=subscription_package,
                    is_active=True)
                return Response({'response': 'You have already Subscribed to this Package'})
            except:
                self.cancelSubscriptions(subscription_service, 'bcs')
                """
                Creating new Subscription
                """
                ser = self.get_serializer(data=request.data)
                ser.is_valid(raise_exception=True)
                self.perform_create(ser)
                subscription_id = request.data['paypal_subscription_id']
                user_subscribed = bcsmodels.SubscriptionOrder.objects.get(paypal_subscription_id=subscription_id)

                notification = bcsmodels.AdminNotification.objects.create(category_choice='bcs',
                                                                          business=self.request.user.business_user.business,
                                                                          notification=f'New Subscription. '
                                                                                       f'<div><a href="https://main.techforing.com/bcs_admin_subscription_detail/{user_subscribed.id}/" target="_blank" class="btn btn-success mt-2">Visit Now</a></div>')
                notification.save()
                return Response(ser.data)


class SubscriptionPurchaseCheckApiView(generics.ListAPIView):
    queryset = bcsmodels.SubscriptionOrder
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        purchased_list = bcsmodels.SubscriptionOrder.objects.filter(user=self.request.user, is_active=True).values_list(
            'subscription_package_id',
            flat=True)
        # print(purchased_list)
        return Response({'result': purchased_list})


class PCSCoursePurchaseCheckApiView(generics.ListAPIView):
    queryset = coursemodels.CoursePurchase
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        purchased_list = coursemodels.CoursePurchase.objects.filter(user=self.request.user).values_list('course_id',
                                                                                                        flat=True)
        print(purchased_list)
        return Response({'result': purchased_list})


class BCSCoursePurchaseCheckApiView(generics.ListAPIView):
    queryset = coursemodels.CoursePurchase
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        purchased_list = coursemodels.CourseOrder.objects.filter(business=self.request.user.business_user.business,
                                                                 is_active=True).values_list('course_package_id',
                                                                                             flat=True)
        print(purchased_list)
        return Response({'result': purchased_list})


class PCSCoursePurchaseApiView(generics.CreateAPIView):
    serializer_class = serializer.PCSCoursePurchaseSerializer
    queryset = coursemodels.CoursePurchase.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        course = request.data['course']
        try:
            check_existing_order = coursemodels.CoursePurchase.objects.get(user=self.request.user, course_id=course)
            return Response({'response': 'You have already purchased this course'})
        except:
            ser = self.get_serializer(data=request.data)
            ser.is_valid(raise_exception=True)
            self.perform_create(ser)
            return Response(ser.data)


class BCSCoursePurchaseApiView(generics.CreateAPIView):
    serializer_class = serializer.BCSCoursePurchaseSerializer
    queryset = coursemodels.CourseOrder.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def cancelSubscriptions(self, course):
        """
        Cancelling Previous Subscriptions
        """
        username = settings.PAYPAL_USER
        password = settings.PAYPAL_PASS
        busername = str(base64.b64encode(bytes(username, 'utf-8')))[1:].replace("'", "").replace("=", '')
        bpassword = str(base64.b64encode(bytes(password, 'utf-8')))[1:].replace("'", "")
        bearer = f"Basic {busername}6{bpassword}"

        packages = coursemodels.CoursePackage.objects.all().values_list(
            'id')

        user_orders = coursemodels.CourseOrder.objects.filter(
            # user__business_user__business=self.request.user.business_user.business,
            business=self.request.user.business_user.business,
            course_package__in=packages,
            course=course,
            is_active=True
        )
        for current_order in user_orders:
            current_order.is_active = False
            current_order.save()
            url = f'{settings.PAYPAL_URL}billing/subscriptions/{current_order.payment_id}/cancel'
            headers = {
                'Content-type': 'application/json',
                'Authorization': bearer
            }
            r = requests.post(url, headers=headers)
            print(r.status_code)
            current_business = bcsmodels.Business.objects.get(business_business__user=self.request.user)
            order_subscription_teams = coursemodels.SubscriptionTeam.objects.filter(business=current_business,
                                                                                    subscription_order=current_order)
            if order_subscription_teams.exists():
                for team in order_subscription_teams:
                    team.delete()
        if user_orders.exists():
            notification = bcsmodels.AdminNotification.objects.create(category_choice='bcs',
                                                                      business=self.request.user.business_user.business,
                                                                      notification=f'User has cancelled the Course '
                                                                                   f'subs'
                                                                                   f'cription for '
                                                                                   f'{current_order.course.course_name}')
            notification.save()

    def perform_create(self, serializer):
        serializer.save(business=self.request.user.business_user.business, is_active=True)

    def create(self, request, *args, **kwargs):
        course = request.data['course']
        course_package = request.data['course_package']
        try:
            check_existing_order = coursemodels.CourseOrder.objects.get(
                business=self.request.user.business_user.business, course=course, course_package=course_package,
                is_active=True)
            return Response({'response': 'You have already purchased this course'})
        except:
            self.cancelSubscriptions(course)
            """
            Creating new Subscription
            """
            ser = self.get_serializer(data=request.data)
            ser.is_valid(raise_exception=True)
            self.perform_create(ser)
            notification = bcsmodels.AdminNotification.objects.create(category_choice='bcs',
                                                                      business=self.request.user.business_user.business,
                                                                      notification=f'New Course Subscription from {self.request.user.business_user.business}')
            notification.save()
            return Response(ser.data)


class BCSCourseApiView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializer.BCSCourseSerializer
    lookup_field = 'id'

    def get_queryset(self):
        service_id = self.kwargs['id']
        return coursemodels.BCSCourse.objects.filter(id=service_id)


class BCSCoursePackageListViewApi(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializer.BCSCoursePackageListSerializer

    # queryset = bcsmodels.SubscriptionBasedPackage.objects.all()

    def get_queryset(self):
        service_id = self.kwargs['id']
        return coursemodels.CoursePackage.objects.filter(service_id=service_id)


class CollectiveNotificationApiView(generics.CreateAPIView):
    permission_classes = [apipermissions.IsMainAdmin]
    serializer_class = serializer.CollectiveNotificationSerializer
    queryset = bcsmodels.Notification


class CollectiveApiView(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        return Response({
            'response': ['PCS', 'BCS']
        })


class IndividualApiView(generics.ListAPIView):
    permission_classes = [apipermissions.IsMainAdmin]
    serializer_class = serializer.IndividualSerializer

    def list(self, request, *args, **kwargs):
        emails = models.User.objects.all()
        ser = self.get_serializer(emails, many=True)
        datas = []
        for email in ser.data:
            datas.append(email['email'])
        return Response({
            'response': datas
        })


class BusinessApiView(generics.ListAPIView):
    permission_classes = [apipermissions.IsMainAdmin]
    serializer_class = serializer.BusinessSerializer

    def list(self, request, *args, **kwargs):
        company_name = bcsmodels.Business.objects.all()
        ser = self.get_serializer(company_name, many=True)
        datas = []
        for email in ser.data:
            datas.append(email['company_name'])
        return Response({
            'response': datas
        })


class InterestApiView(generics.ListAPIView):
    permission_classes = [apipermissions.IsMainAdmin]

    def list(self, request, *args, **kwargs):
        return Response({
            'response': [field.name for field in accountmodel.Interest._meta.get_fields() if
                         field.name != 'id' and field.name != 'user']
        })


class SubscriptionTeamOrderApiView(generics.ListAPIView):
    serializer_class = serializer.SubscriptionTeamOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        business = self.request.user.business_user.business
        return bcsmodels.SubscriptionOrder.objects.filter(user__business_user__business=business, category_choice='bcs')


class CourseSubscriptionTeamOrderApiView(generics.ListAPIView):
    serializer_class = serializer.CourseSubscriptionTeamOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        business = self.request.user.business_user.business
        return coursemodels.CourseOrder.objects.filter(business=business)


class SubscriptionTeamAccessApiView(generics.ListCreateAPIView):
    serializer_class = serializer.SubscriptionTeamAccessSerializer
    permission_classes = [apipermissions.IsTeamAdmin]

    def perform_create(self, serializer):
        serializer.save(business=self.request.user.business_user.business)

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        data = ser.is_valid(raise_exception=True)
        business = bcsmodels.UsersBusiness.objects.get(user_id=request.data.get('user'))

        if self.request.user.business_user.business == business.business:
            service_id = request.data['subscription_order']
            is_subscribed = bcsmodels.SubscriptionTeam.objects.filter(subscription_order_id=service_id,
                                                                      user_id=request.data.get('user'))
            if is_subscribed.exists():
                return Response({
                    'response': 'Team member already assigned'
                })
            else:
                self.perform_create(ser)
                user = bcsmodels.User.objects.get(id=ser.data['user'])
                business = bcsmodels.Business.objects.get(id=ser.data['business'])
                subscription_order = ser.data['subscription_order']
                notification = bcsmodels.Notification.objects.create(category_choice=user.email,
                                                                     notification_time=timezone.now(),
                                                                     notification=f'Your Business {business.company_name}. '
                                                                                  f'Has added you to an service. '
                                                                                  f'Please Fill the form to get the '
                                                                                  f'service. '
                                                                                  f'<div><a href="https://main.techforing'
                                                                                  f'.com/bcs_user_team_service_form/{subscription_order}/" target="_blank" class="btn btn-success mt-2">Visit Now</a></div>')
                notification.save()
                return Response(ser.data)
        else:
            return Response({
                'response': 'User is not in your business'
            })

    def get_queryset(self):
        business = self.request.user.business_user.business
        return bcsmodels.SubscriptionTeam.objects.filter(business=business)


class CourseSubscriptionTeamAccessApiView(generics.ListCreateAPIView):
    serializer_class = serializer.CourseSubscriptionTeamAccessSerializer
    permission_classes = [apipermissions.IsTeamAdmin]

    def perform_create(self, serializer):
        serializer.save(business=self.request.user.business_user.business)

    def create(self, request, *args, **kwargs):
        ser = self.get_serializer(data=request.data)
        data = ser.is_valid(raise_exception=True)
        business = bcsmodels.UsersBusiness.objects.get(user_id=request.data.get('user'))

        if self.request.user.business_user.business == business.business:
            service_id = request.data['subscription_order']
            is_subscribed = coursemodels.SubscriptionTeam.objects.filter(subscription_order_id=service_id,
                                                                         user_id=request.data.get('user'))
            if is_subscribed.exists():
                return Response({
                    'response': 'Team member already assigned'
                })
            else:
                self.perform_create(ser)
                user = bcsmodels.User.objects.get(id=ser.data['user'])
                business = bcsmodels.Business.objects.get(id=ser.data['business'])
                subscription_order = ser.data['subscription_order']
                current_course = coursemodels.BCSCourse.objects.get(courseorder_bcscourse__id=subscription_order)
                notification = bcsmodels.Notification.objects.create(category_choice=user.email,
                                                                     notification_time=timezone.now(),
                                                                     notification=f'Your Business {business.company_name}. '
                                                                                  f'Has added you to an Course. '
                                                                                  f'Please Fill visit the link. '
                                                                                  f'<div><a href="https://training.techforing'
                                                                                  f'.com/academy_user_files/{current_course.id}/" target="_blank" class="btn btn-success mt-2">Visit Now</a></div>')
                notification.save()
                return Response(ser.data)
        else:
            return Response({
                'response': 'User is not in your business'
            })

    def get_queryset(self):
        business = self.request.user.business_user.business
        return coursemodels.SubscriptionTeam.objects.filter(business=business)


class TeamInputInfoApiView(generics.ListAPIView):
    serializer_class = serializer.TeamInputInfoSerializer
    permission_classes = [apipermissions.IsBCSAdmin]

    # lookup_field = 'pk'
    # queryset = bcsmodels.TeamSubscriptionInput.objects.all()

    def get_queryset(self):
        subscription_team_id = self.kwargs.get('id')
        current_team_member = bcsmodels.SubscriptionTeam.objects.get(id=subscription_team_id)
        return bcsmodels.TeamSubscriptionInput.objects.filter(user=current_team_member.user)
