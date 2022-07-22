from django.urls import path, include,re_path
from Academy import views

urlpatterns = [
    path('', views.academyHomeView, name='academy_home'),

    path('tinymce/', include('tinymce.urls')),
    re_path(r'^(pages/)?ccsp(.*)?/', views.ccspView, name='ccsp'),

    re_path(r'^(pages/)?academy_faq(.*)?/', views.academyFAQView, name='academy_faq'),
    re_path(r'^(pages/)?corporate_training(.*)?/', views.corporateTrainingView, name='corporate_training'),
    re_path(r'^(pages/)?law_enforcement(.*)?/', views.lawEnforcementView, name='law_enforcement'),
    re_path(r'^(pages/)?educational_institute(.*)?/', views.educationalInstituteView, name='educational_institute'),

    path('download/', views.download_file, name='demo_download'),
    path('download/<str:path>', views.download_file, name='download'),


    path('academy_user_files/<str:section>/<str:module>/<str:content_type>', views.course_material,
         name='course_material'),
    path('academy_user_exams/', views.UserExams, name='academy_user_exams'),
    path('academy_user_events/', views.UserEvents, name='academy_user_events'),
    path('academy_user_notifications/', views.UserNotifications, name='academy_user_notifications'),
    path('academy_user_settings/', views.UserSettings, name='academy_user_settings'),

    # bcs academy user panel
    path('academy_user_courses/', views.UserCourses, name='academy_user_courses'),
    path('academy_user_courses/<id>/', views.UserCoursesDetails, name='academy_user_courses_details'),
    path('academy_my_courses/', views.myCourses, name='academy_my_courses'),
    path('academy_user_files/', views.UserFiles, name='academy_user_files'),
    path('academy_user_files/<id>/', views.UserFiles, name='academy_user_files'),
]
