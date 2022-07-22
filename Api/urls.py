from django.urls import path
from Api import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'api_app'

urlpatterns = [
    path('blogs/posts/', views.PostApi.as_view(), name='post_api'),
    path('blogs/category/', views.CategoryApi.as_view(), name='category_api'),
    path('blogs/category/<id>/', views.SubCategoryApi.as_view(), name='sub_category_api'),
    path('blogs/category/<id>/<sub_id>/', views.FilterApi.as_view(), name='sub_filter_api'),
    path('blogs/comment/', views.AllCommentCreateViewApi.as_view(), name='all_comment_create_view_api'),
    path('blogs/comment/<post_id>/', views.CommentCreateViewApi.as_view(), name='comment_create_view_api'),
    path('blogs/filter/<category>/<text>/', views.BlogFilterApiView.as_view(), name='blog_filter_view_api'),
    path('blogs/filter/date/<category>/<text>/', views.BlogFilterDateApiView.as_view(),
         name='blog_filter_date_view_api'),

    path('bcs/package/<id>/', views.PackageListViewApi.as_view(), name='package_list_api'),
    path('bcs/subscription_service/<id>/', views.SubscriptionServiceApiView.as_view(), name='subscription_service'),

    path('bcs/services/<cat>/', views.ServiceListApiView.as_view(), name='service_list_api'),
    path('bcs/sub_service/<id>/', views.SubServiceApiView.as_view(), name='subservice_list_api'),
    path('bcs/sub_service_input/<id>/', views.SubServiceInputApiView.as_view(), name='subservice_input_list_api'),
    path('bcs/choice_field/<id>/', views.ChoiceApiView.as_view(), name='choice_field'),

    path('bcs/user_order/<id>/', views.UserSubServiceOrderApiView.as_view(), name='user_order'),  # Not

    path('bcs/team_permission/<id>/', views.TeamPermissionApiView.as_view(), name='team_permission'),

    path('bcs/bcs_admin_all_chart/', views.BCSAdminDashboardAllChartApiView.as_view(), name='bcs_admin_all_chart'),
    path('bcs/bcs_admin_year_chart/', views.BCSAdminDashboardYearChartApiView.as_view(), name='bcs_admin_year_chart'),
    path('bcs/bcs_admin_month_chart/', views.BCSAdminDashboardMonthChartApiView.as_view(),
         name='bcs_admin_month_chart'),
    path('bcs/bcs_admin_lastmonth_chart/', views.BCSAdminDashboardLastMonthChartApiView.as_view(),
         name='bcs_admin_lastmonth_chart'),
    path('bcs/bcs_admin_range_chart/', views.BCSAdminDashboardRangeChartApiView.as_view(),
         name='bcs_admin_chart_range'),
    

    path('pcs/pcs_admin_all_chart/', views.PCSAdminDashboardAllChartApiView.as_view(), name='pcs_admin_all_chart'),
    path('pcs/pcs_admin_year_chart/', views.PCSAdminDashboardYearChartApiView.as_view(), name='pcs_admin_year_chart'),
    path('pcs/pcs_admin_month_chart/', views.PCSAdminDashboardMonthChartApiView.as_view(),
         name='pcs_admin_month_chart'),
    path('pcs/pcs_admin_lastmonth_chart/', views.PCSAdminDashboardLastMonthChartApiView.as_view(),
         name='pcs_admin_lastmonth_chart'),
    path('pcs/pcs_admin_range_chart/', views.PCSAdminDashboardRangeChartApiView.as_view(),
         name='pcs_admin_range_chart'),

    path('main/main_admin_all_chart/', views.MainAdminDashboardAllChartApiView.as_view(), name='main_admin_all_chart'),
    path('main/main_admin_year_chart/', views.MainAdminDashboardYearChartApiView.as_view(),
         name='main_admin_year_chart'),
    path('main/main_admin_month_chart/', views.MainAdminDashboardMonthChartApiView.as_view(),
         name='main_admin_month_chart'),
    path('main/main_admin_lastmonth_chart/', views.MainAdminDashboardLastMonthChartApiView.as_view(),
         name='main_admin_lastmonth_chart'),
    path('main/main_admin_range_chart/', views.MainAdminDashboardRangeChartApiView.as_view(),
         name='main_admin_range_chart'),     

    path('bcs/bcs_subscriptions/<service>/', views.SubscriptionApiView.as_view(), name='bcs_subscriptions'),

    path('subscription_order/', views.SubscriptionOrderView.as_view(), name='subscription_order'),
    path('subscription_order_check/', views.SubscriptionPurchaseCheckApiView.as_view(), name='subscription_order_check'),
    path('pcs/course_order_check/', views.PCSCoursePurchaseCheckApiView.as_view(), name='course_order_check'),
    path('pcs/course_order/', views.PCSCoursePurchaseApiView.as_view(), name='course_order'),
    path('bcs/course_order_check/', views.BCSCoursePurchaseCheckApiView.as_view(), name='bcs_course_order_check'),
    path('bcs/course_order/', views.BCSCoursePurchaseApiView.as_view(), name='bcs_course_order'),

    path('bcs/bcs_course/<id>/', views.BCSCourseApiView.as_view(), name='bcs_course'),
    path('bcs/course_package/<id>/', views.BCSCoursePackageListViewApi.as_view(), name='course_package_list_api'),

    path('main/collective/', views.CollectiveApiView.as_view(), name='collective'),
    path('main/individual/', views.IndividualApiView.as_view(), name='individual'),
    path('main/business/', views.BusinessApiView.as_view(), name='business'),
    path('main/interest/', views.InterestApiView.as_view(), name='interest'),
    path('main/collective_notification/', views.CollectiveNotificationApiView.as_view(), name='collective_notification'),

    path('bcs/puchased_subscriptions/', views.SubscriptionTeamOrderApiView.as_view(), name='purchased_subscriptions'),
    path('bcs/puchased_course_subscriptions/', views.CourseSubscriptionTeamOrderApiView.as_view(),
         name='puchased_course_subscriptions'),
    path('bcs/subscription_team/', views.SubscriptionTeamAccessApiView.as_view(), name='subscription_team'),
    path('bcs/course_subscription_team/', views.CourseSubscriptionTeamAccessApiView.as_view(), name='course_subscription_team'),
    path('bcs/subscription_input/<id>/', views.SubscriptionInputApiView.as_view(), name='subscription_input'),

    path('bcs/team_input_info/<id>/', views.TeamInputInfoApiView.as_view(), name='team_input_info'),
]
